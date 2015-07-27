from __future__ import unicode_literals
from django.core.cache import cache
from django.utils.timezone import is_aware, utc
import datetime
from django.conf import settings

from django.contrib.auth.models import User
from apps_data.courseevent.models.courseevent import CourseEvent
from model_utils.models import TimeStampedModel
from django.db import models
from django.core.exceptions import ValidationError


def calc_subforum_ancestors(subforum_id):
    subforum = SubForum.objects.get(id=subforum_id)
    ancestors_qs = subforum.get_ancestors_qs().order_by('display_nr')
    return display_ancestors(ancestors_qs)


def validate_parentforum(value):
    depth = len(calc_subforum_ancestors(value))
    if depth > 1:
        msg = str('Derzeit kann die Tiefe von Unterforen nicht mehr als 3 Stufen betragen')
        raise ValidationError(msg)



class Forum(TimeStampedModel):
    """
    The Forum has been designed as an independent starting point:
    independent of say courseevents, that forums are normally
    assigned to via the classroom app.

    Forums do not need a slug, since they runs under the slug of the
    object they are assigned to.

    Title and Text field serve the purpose, that they can be set
    by instructors according to their preferences.

    Forums may be subforums to other forums.
    """
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True)
    courseevent = models.ForeignKey(CourseEvent, related_name="kursforum")

    class Meta:
        verbose_name = "XForum"

    def __unicode__(self):
        return u'%s' % (self.title)

    def get_decendants_qs(self):
        subforums = self.subforum_set.all()
        return subforums


class SubForum(TimeStampedModel):
    """
    The Forum has been designed as an independent starting point:
    independent of say courseevents, that forums are normally
    assigned to via the classroom app.

    Forums do not need a slug, since they runs under the slug of the
    object they are assigned to.

    Title and Text field serve the purpose, that they can be set
    by instructors according to their preferences.

    Forums may be subforums to other forums.
    """
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True)
    parentforum = models.ForeignKey('self', null=True, blank=True, validators=[validate_parentforum])
    display_nr = models.IntegerField()
    forum = models.ForeignKey(Forum)
    can_have_threads = models.BooleanField(default=True)

    class Meta:
        verbose_name = "XSubForum"

    def __unicode__(self):
        if self.parentforum:
            return u'%s / %s' % (self.parentforum, self.title)
        else:
            return u'%s' % (self.title)

    def get_ancestors_qs(self):
        #gets all ancestors of a subforum as queryset
        if self.parentforum is None:
            return SubForum.objects.none()
        return SubForum.objects.filter(id=self.parentforum.id) | self.parentforum.get_ancestors_qs()


class ForumContributionModel(TimeStampedModel):
    text = models.TextField()

    forum = models.ForeignKey(Forum)

    class Meta:
        abstract=True

    def time_since(self):
        return timesince(self.modified)


class Thread(ForumContributionModel):
    """This is a thread. A thread still has its own url, but not with a slug, rather it has just an id."""
    title = models.CharField(max_length=100)
    subforum = models.ForeignKey(SubForum)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="beitragsautor")
    #!!! modified of Thread must be updated for save method of Comment and Post!!!

    class Meta:
        verbose_name = "XThread"


    def __unicode__(self):
        return u'%s' % (self.title)

    def timesince_created(self):
        return timesince(self.created)

    def timesince_modified(self):
        return timesince(self.modified)

    def post_count(self):
        count = Post.objects.filter(thread=self.id).count()
        return count




class Post(ForumContributionModel):
    """These are the posts under a thread. They are only shown on the threads page and have no url
    on their own."""
    thread = models.ForeignKey(Thread)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="postautor")

    class Meta:
        verbose_name = "XPost"

    def __unicode__(self):
        return u'%s' % (self.thread_id)

    def timesince_created(self):
        return timesince(self.created)

    def timesince_modified(self):
        return timesince(self.modified)


def display_ancestors(ancestors_qs):
    """
    forms a dictionary for the breadcrumb of subforums
    """
    subforum_breadcrumb = []
    if ancestors_qs.exists():
        for subforum in ancestors_qs:
            subforum_breadcrumb.append({
                'title': subforum.title,
                'id': subforum.id,
            })
    return subforum_breadcrumb



