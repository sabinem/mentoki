# coding: utf-8

from __future__ import unicode_literals, absolute_import

from itertools import chain
from operator import attrgetter

from django.conf import settings
from django.core.validators import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.core.urlresolvers import reverse

from model_utils.models import TimeStampedModel
from model_utils.managers import QueryManager
from model_utils.fields import MonitorField
from mptt.models import MPTTModel, TreeForeignKey, TreeManager

from apps_data.courseevent.models.courseevent import CourseEvent


class ForumManager(TreeManager):

    def forums_for_courseevent(self, courseevent):
        return self.filter(courseevent=courseevent, level=0).\
            get_descendants(include_self=True)

    def classroom_menu(self, courseevent):
        return self.filter(courseevent=courseevent, level=1)

    def published_forum_ids(self, courseevent):
        # fetched here in order to avoid circular import
        from apps_data.courseevent.models.menu import ClassroomMenuItem
        published_forum_ids = \
            ClassroomMenuItem.objects.forums_for_courseevent(
                courseevent=courseevent).values_list('forum_id', flat=True)
        return self.filter(id__in=published_forum_ids).\
            get_descendants().values_list('id', flat=True)

    def published_forums(self, courseevent):
        # fetched here in order to avoid circular import
        from apps_data.courseevent.models.menu import ClassroomMenuItem
        published_forum_ids = \
            ClassroomMenuItem.objects.forums_for_courseevent(
                courseevent=courseevent).values_list('forum_id', flat=True)
        print "========================"
        print published_forum_ids
        return self.filter(id__in=published_forum_ids).\
            get_descendants(include_self=True)


    def active_forums_for_courseevent(self, courseevent):
        return self.filter(courseevent=courseevent, level=0, hidden=False).\
            get_descendants(include_self=True)

    def forums_published_in_courseevent(self, courseevent):
        return self.filter(courseevent=courseevent)

    def create(self, courseevent, title, display_nr,
               parent,  can_have_threads=True, text="", description=""):
        forum = Forum(courseevent=courseevent,
                      text=text,
                      title=title,
                      description=description,
                      display_nr=display_nr,
                      can_have_threads=can_have_threads)
        forum.insert_at(parent)
        forum.save()
        Forum.objects.rebuild()

        return forum


class Forum(MPTTModel, TimeStampedModel):

    courseevent = models.ForeignKey(CourseEvent)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True, verbose_name="einhängen unter")

    title = models.CharField(
        verbose_name="Forums-Titel",
        max_length=100
    )
    text = models.TextField(
        verbose_name="Ausführliche Beschreibung des Forums",
        help_text="""Dieser Text wird den Forumsbeiträgen vorangestellt und leitet die Kursteilnehmern an, ihre
                  Beiträge zu schreiben.""",
        blank=True
    )
    description = models.CharField(
        verbose_name="Kurzbeschreibung",
        help_text="Die Kurzbeschreibung erscheint auf der Übersichtsseite der Foren.",
        max_length=200,
        blank=True
    )
    display_nr = models.IntegerField(
        verbose_name="Anzeigereihenfolge",
        help_text="nicht nach aussen sichtbar"
    )

    can_have_threads = models.BooleanField(
        verbose_name="Beiträge erlaubt",
        help_text="""Steuert, ob Beiträge in diesem Unterforum gemacht werden können,
                  oder ob es nur zur Gliederung dient.""",
        default=True)

    objects = ForumManager()
    forum = QueryManager(level=0)
    subforum = QueryManager(level__gte=1)
    parent_choice_new = QueryManager(level__lte=1).order_by('tree_id', 'level', 'display_nr')

    class Meta:
        verbose_name = "Forum"
        verbose_name_plural = "Foren"

    class MPTTMeta:
        order_insertion_by = ['courseevent', 'display_nr']

    def __unicode__(self):
        return u'%s' % (self.title)

    def get_absolute_url(self):
        return reverse('coursebackend:forum:detail',
                       kwargs={'course_slug':self.course_slug, 'slug': self.slug, 'pk':self.pk })

    def get_next_sibling(self):
        next = super(Forum, self).get_next_sibling()
        try:
            if next.courseevent_id == self.courseevent_id:
                return next
            else:
                return None
        except:
            return None

    def get_previous_sibling(self):
        previous = super(Forum, self).get_previous_sibling()
        try:
            if previous.courseevent_id == self.courseevent_id:
                return previous
            else:
                return None
        except:
            return None

    def get_breadcrumbs_with_self(self):
        return self.get_ancestors(include_self=True)

    def get_published_breadcrumbs_with_self(self):
        return self.get_ancestors(include_self=True).filter(level__gt=0)

    @property
    def thread_count(self):
        return Thread.objects.filter(forum=self).count()

    @property
    def decendants_thread_count(self):
        decendants_ids = self.get_descendants(include_self=True).values_list('id', flat=True)
        return Thread.objects.filter(forum__in=decendants_ids).count()

    def get_absolute_url(self):
        return reverse('coursebackend:forum:detail',
                       kwargs={'course_slug':self.course_slug,
                               'slug':self.slug,
                               'pk':self.pk})

    @property
    def is_visible_in_classroom(self):
        """
        decides whether forum is visible in classroom
        """
        # fetched here in order to avoid circular import
        if self.level == 1:
            level1_forum = self
        else:
            level1_forum = self.get_ancestors().get(level=1)
        # fetched here in order to avoid circular import
        from apps_data.courseevent.models.menu import ClassroomMenuItem
        menuitems = \
            ClassroomMenuItem.objects.forum_ids_published_in_class(courseevent=self.courseevent)
        if level1_forum.id in menuitems:
            return True
        else:
            return False

    def clean(self):
        if not self.can_have_threads:
            if self.thread_count > 0:
                raise ValidationError('Dieses Forum hat bereits Beiträge.')


class ForumContributionModel(TimeStampedModel):

    courseevent = models.ForeignKey(CourseEvent)

    hidden = models.BooleanField(
        verbose_name=_('versteckt'),
        default=False)
    hidden_status_changed = MonitorField(monitor='hidden')

    text = models.TextField()

    class Meta:
        abstract=True


class ThreadManager(models.Manager):

    def create_new_thread(self, courseevent, forum,
                        text, title, author):
        thread = Thread(courseevent=courseevent, forum=forum, text=text, title=title, author=author)
        thread.save()
        return thread

    def recent_contributions(self, courseevent):

        threads = self.select_related('author').\
            filter(courseevent=courseevent).\
            order_by('-modified')[0:50]
        posts = Post.objects.filter(courseevent=courseevent).\
            select_related('thread','author').order_by('-modified')[0:50]
        contributions = sorted(
            chain(threads, posts),
            key=attrgetter('modified'))
        return contributions


    def recent_published_contributions(self, courseevent):
        published_forum_ids = Forum.objects.published_forum_ids(courseevent=courseevent)
        threads = self.select_related('author').\
            filter(courseevent=courseevent, forum_id__in=published_forum_ids).\
            order_by('-modified')[0:20]
        posts = Post.objects.filter(courseevent=courseevent,
                                    thread__forum_id__in=published_forum_ids).\
            select_related('thread','author').order_by('-modified')[0:50]
        contributions = sorted(
            chain(threads, posts),
            key=attrgetter('modified'))
        return contributions


class Thread(ForumContributionModel):

    forum = models.ForeignKey(
        Forum,
        on_delete=models.PROTECT
    )

    title = models.CharField(
        verbose_name="Titel für Deinen Beitrag",
        max_length=100)

    post_count = models.IntegerField(default=0)
    last_author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="last_post_author", blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="thread_author")

    objects = ThreadManager()

    class Meta:
        verbose_name = "Beitrag (Forum)"
        verbose_name_plural = "Beiträge (Forum)"
        ordering = [ '-modified' ]

    def __unicode__(self):
        return u'%s: %s %s' % (str(self.courseevent_id), str(self.id), self.title)

    def save(self):
        self.courseevent = self.forum.courseevent
        if not self.last_author:
            self.last_author = self.author
        super(Thread, self).save()

    def clean(self):
        """
        strip blanks before and after input
        """
        if self.text:
            self.text = self.text.strip()
        if self.title:
            self.title = self.title.strip()


class PostManager(models.Manager):

    def create_new_post(self, courseevent, thread,
                        text, title, author):
        post = Post(courseevent=courseevent, thread=thread, text=text, title=title, author=author)
        post.save()
        return post

    def contributors_emails(self, thread):
        return set(self.filter(thread=thread).select_related('author')\
            .values_list('author__email', flat=True))


class Post(ForumContributionModel):

    title = models.CharField(max_length=100)

    thread = models.ForeignKey(
        Thread,
        on_delete=models.PROTECT
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="post_author",
        on_delete=models.PROTECT
    )

    objects = PostManager()

    class Meta:
        verbose_name = "Post (Forum)"
        verbose_name_plural = "Posts (Forum)"
        ordering = [ '-modified' ]

    def __unicode__(self):
        return u'%s: %s: %s' % (str(self.courseevent_id), str(self.thread_id), self.title)

    def save(self):
        self.courseevent = self.thread.courseevent
        thread = self.thread
        thread.post_count = Post.objects.filter(thread=self.thread).count() + 1
        thread.last_author = self.author
        thread.save()
        super(Post, self).save()



