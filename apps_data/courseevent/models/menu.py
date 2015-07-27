# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.fields import MonitorField
from model_utils import Choices
from model_utils.models import TimeStampedModel

from apps_data.course.models.lesson import Lesson

from .courseevent import CourseEvent
from .forum import Forum
from .homework import Homework



class ClassroomMenuItemManager(models.Manager):

    def published(self, courseevent):
        return self.filter(courseevent=courseevent, published=True).order_by('item_nr')

    def courseevent(self, courseevent):
        return self.filter(courseevent=courseevent).order_by('item_nr')


class ClassroomMenuItem(TimeStampedModel):
    """
    Classroom Menu
    """
    courseevent = models.ForeignKey(CourseEvent)

    lesson = models.ForeignKey(Lesson, blank=True, null=True)
    forum = models.ForeignKey(Forum, blank=True, null=True)
    homework = models.ForeignKey(Homework, blank=True, null=True )

    MENU_ITEM_TYPE = Choices(('forum', 'forum_item', _('forum')),
                     ('lesson', 'lesson_item', _('lesson or lesson block')),
                     ('anouncements', 'announcements', _('announcements')),
                     ('homework', 'homework', _('homework')),
                     ('last_posts', 'forum_last_posts', _('latest forum posts'))
                    )

    item_type = models.CharField(choices=MENU_ITEM_TYPE, max_length=15)
    display_nr = models.IntegerField()
    display_title = models.CharField(max_length=200, default="x")

    published = models.BooleanField(default=False)
    published_at = MonitorField(monitor='published', when=[True])

    is_start_item =models.BooleanField()

    objects = ClassroomMenuItemManager()

    def __unicode__(self):
        return u'menu %s / %s' % (self.courseevent, str(self.item_nr))





