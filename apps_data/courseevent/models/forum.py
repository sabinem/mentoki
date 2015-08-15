# coding: utf-8

from __future__ import unicode_literals, absolute_import

from itertools import chain
from operator import attrgetter

from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel
from model_utils.managers import QueryManager
from model_utils.fields import MonitorField

from mptt.models import MPTTModel, TreeForeignKey, TreeManager

from .courseevent import CourseEvent

from apps.forum.models import Forum as OldForum
from apps.forum.models import SubForum as OldSubForum
from apps.forum.models import Post as OldPost
from apps.forum.models import Thread as OldThread


class ForumManager(TreeManager):

    def forums_for_courseevent(self, courseevent):
        return self.filter(courseevent=courseevent, level=0).\
            get_descendants(include_self=True)

    def active_forums_for_courseevent(self, courseevent):
        return self.filter(courseevent=courseevent, level=0, hidden=False).\
            get_descendants(include_self=True)

    def forums_published_in_courseevent(self, courseevent):
        return self.filter(courseevent=courseevent, published=True)

    def create(self, courseevent, text, title, description, display_nr, can_have_threads=False,
               parent=None):
        forum = Forum(courseevent=courseevent,
                      text=text,
                      title=title,
                      description=description,
                      published=False,
                      display_nr=display_nr,
                      can_have_threads=can_have_threads)
        forum.insert_at(parent)
        forum.save()

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
    #thread_count = models.IntegerField(default=0)

    hidden = models.BooleanField(
        verbose_name=_('versteckt'),
        default=False)
    hidden_status_changed = MonitorField(monitor='hidden')

    published = models.BooleanField(
        verbose_name="veröffentlicht",
        help_text="""Zeigt an, ob das Forum im Klassenzimmer sichtbar ist.""",
        default=False
    )
    publish_status_changed = MonitorField(monitor='published')

    oldforum = models.ForeignKey(OldForum, blank=True, null=True)
    oldsubforum = models.ForeignKey(OldSubForum, blank=True, null=True, related_name="Unterforum_alt")

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

    @cached_property
    def slug(self):
        return self.courseevent.slug


    @cached_property
    def course_slug(self):
        return self.courseevent.course_slug

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

    @cached_property
    def is_forum(self):
        if self.get_level() == 0:
            return True
        else:
            return False

    @cached_property
    def is_subforum(self):
        if self.get_level() >= 1:
            return True
        else:
            return False

    def thread_count(self):
        return Thread.objects.filter(forum=self).count()

    def get_absolute_url(self):
        return reverse('coursebackend:forum:detail',
                       kwargs={'course_slug':self.course_slug,
                               'slug':self.slug,
                               'pk':self.pk})

    def get_classroom_url(self):
        return reverse('classroom:forum:detail',
               kwargs={'slug':self.slug,
                       'pk':self.pk})


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
            filter(courseevent=courseevent, hidden=False).\
            order_by('-modified')[0:50]
        posts = Post.objects.filter(courseevent=courseevent).\
            select_related('thread','author').order_by('-modified')[0:50]
        contributions = sorted(
            chain(threads, posts),
            key=attrgetter('modified'))
        return contributions


class Thread(ForumContributionModel):

    forum = models.ForeignKey(Forum)

    title = models.CharField(
        verbose_name="Titel für Deinen Beitrag",
        max_length=100)

    post_count = models.IntegerField(default=0)
    last_author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="last_post_author", blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="thread_author")

    # delete later on
    oldthread = models.ForeignKey(OldThread, blank=True, null=True)

    objects = ThreadManager()

    class Meta:
        verbose_name = "Beitrag"
        verbose_name_plural = "Beiträge"
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


class Post(ForumContributionModel):

    title = models.CharField(max_length=100)

    thread = models.ForeignKey(Thread)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="post_author")

    # will be deleted later on
    oldpost = models.ForeignKey(OldPost, blank=True, null=True)

    objects = PostManager()

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
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


def last_contributions(courseevent):
    return ForumContributionModel.objects.filter(courseevent=courseevent).select_subclasses().\
    order_by('created')


