# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.db import models
from django.utils.translation import ugettext as _

from model_utils.models import TimeStampedModel
from model_utils.fields import MonitorField, StatusField
from model_utils import Choices


from apps_data.courseevent.models.courseevent import CourseEvent


class AnnouncementManager(models.Manager):

    def published(self, courseevent):
        return self.filter(courseevent=courseevent, published=True).order_by('published_at')

    def unpublished(self, courseevent):
        return self.filter(courseevent=courseevent, published=False).order_by('created')

    def create(self, courseevent, text, title, published=False):
        announcement = Announcement(courseevent=courseevent,
                                    text=text,
                                    title=title,
                                    published=published)
        announcement.save()
        return announcement

class Announcement(TimeStampedModel):

    courseevent = models.ForeignKey(CourseEvent)

    title = models.CharField(verbose_name="Betreff",
                             max_length=100)
    text = models.TextField(verbose_name="Text")

    published = models.BooleanField(verbose_name="veröffentlichen?", default=False)
    published_at = MonitorField(verbose_name="veröffentlicht am", monitor='published', when=[True])

    objects = AnnouncementManager()

    def __unicode__(self):
        return self.title
