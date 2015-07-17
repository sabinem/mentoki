# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.db import models
from django.conf import settings
from django.utils.functional import cached_property
from django.core.urlresolvers import reverse

from model_utils.models import TimeStampedModel
from model_utils.managers import PassThroughManager
from autoslug import AutoSlugField

from django.contrib.auth.models import User

from django.db import models
from mptt.models import MPTTModel, TreeForeignKey, TreeManager
from django.utils.functional import cached_property
from django.template.defaultfilters import slugify

from model_utils.models import TimeStampedModel
from model_utils.managers import InheritanceManager
from model_utils.managers import PassThroughManager

from django.core.urlresolvers import reverse

from .courseevent import CourseEvent
from apps.forum.models import Forum as OldForum
from apps.forum.models import SubForum as OldSubForum
from apps.forum.models import Post as OldPost
from apps.forum.models import Thread as OldThread


from model_utils.managers import QueryManager

from django.db.models import Q


class Forum(MPTTModel, TimeStampedModel):

    courseevent = models.ForeignKey(CourseEvent)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True, verbose_name="einhängen unter")

    title = models.CharField(max_length=100)
    text = models.TextField(blank=True)

    display_nr = models.IntegerField()

    can_have_threads = models.BooleanField(default=True)

    oldforum = models.ForeignKey(OldForum, blank=True, null=True)
    oldsubforum = models.ForeignKey(OldSubForum, blank=True, null=True, related_name="Unterforum_alt")

    objects = TreeManager()
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

    @cached_property
    def slug(self):
        return self.courseevent.slug

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
    author = models.ForeignKey(settings.AUTH_USER_MODEL)

    objects = InheritanceManager()

    class Meta:
        abstract=True


class Thread(ForumContributionModel):

    forum = models.ForeignKey(Forum)

    title = models.CharField(max_length=100)

    # delete later on
    oldthread = models.ForeignKey(OldThread, blank=True, null=True)

    def __unicode__(self):
        return u'%s' % (self.title)

    def save(self):
        self.courseevent = self.forum.courseevent
        super(Thread, self).save()

    @cached_property
    def post_count(self):
        count = Post.objects.filter(thread=self.id).count()
        return count


class Post(ForumContributionModel):

    thread = models.ForeignKey(Thread)

    # will be deleted later on
    oldpost = models.ForeignKey(OldPost, blank=True, null=True)

    def __unicode__(self):
        return u'%s zu %s' % (self.author, self.thread)

    def save(self):
        self.courseevent = self.thread.courseevent
        super(Post, self).save()


def last_contributions(courseevent):
    return ForumContributionModel.objects.filter(courseevent=courseevent).select_subclasses().\
    order_by('created')
