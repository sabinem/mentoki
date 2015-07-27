# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.db import models
from django.utils.translation import ugettext as _

from model_utils.models import TimeStampedModel
from model_utils.fields import MonitorField, StatusField
from model_utils import Choices


from apps_data.courseevent.models import CourseEvent


class HomeworkManager(models.Manager):

    def published(self, courseevent):
        return self.filter(courseevent=courseevent, status=Announcement.STATUS.draft).order_by('published_at')

    def unpublished(self, courseevent):
        return self.filter(courseevent=courseevent, status=Announcement.STATUS.published).order_by('created')


class Homework(TimeStampedModel):

    course = models.ForeignKey(CourseEvent)

    title = models.CharField(max_length=100, verbose_name="Thema")
    text = models.TextField(verbose_name="Text der Ankündigung: Vorsicht Bilder werden noch nicht mitgeschickt")

    objects = HomeworkManager()

    def __unicode__(self):
        return self.title
