# coding: utf-8

from __future__ import unicode_literals, absolute_import

from itertools import chain
from operator import attrgetter

from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.functional import cached_property

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

    def forums_published_in_courseevent(self, courseevent):
        return self.filter(courseevent=courseevent, published=True)


class Forum(MPTTModel, TimeStampedModel):

    courseevent = models.ForeignKey(CourseEvent)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True, verbose_name="einhängen unter")

    title = models.CharField(max_length=100)
    text = models.TextField(blank=True)

    display_nr = models.IntegerField()

    can_have_threads = models.BooleanField(default=True)
    #thread_count = models.IntegerField(default=0)

    published = models.BooleanField(default=False)
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
        return u'%s: %s' % (str(self.courseevent_id), self.title)

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

    def possible_parents(self):
        qs = Forum.objects.none()
        if self.is_forum:
            pass
        elif self.is_leaf_node():
           qs = Forum.objects.filter(level__lte=1, courseevent=self.courseevent)
        else:
           qs = Forum.objects.filter(level=0, courseevent=self.courseevent)
        return qs.exclude(pk=self.pk).order_by('tree_id', 'level', 'display_nr')


class ForumContributionModel(TimeStampedModel):

    courseevent = models.ForeignKey(CourseEvent)

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


