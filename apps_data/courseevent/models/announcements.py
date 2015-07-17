# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.db import models
from django.utils.translation import ugettext as _

from model_utils.models import TimeStampedModel
from model_utils.managers import PassThroughManager
from model_utils.fields import MonitorField, StatusField
from model_utils import Choices


from apps_data.courseevent.models import CourseEvent
from ..managers import AnnouncementQuerySet


class Announcement(TimeStampedModel):

    courseevent = models.ForeignKey(CourseEvent)

    title = models.CharField(max_length=100, verbose_name="Thema")
    text = models.TextField(verbose_name="Text der Ankündigung: Vorsicht Bilder werden noch nicht mitgeschickt")

    STATUS = Choices(('draft', _('draft')), ('published', _('published')))

    status = StatusField(choices_name='STATUS')
    published_at = MonitorField(monitor='status', when=['published'])

    objects = PassThroughManager.for_queryset_class(AnnouncementQuerySet)()

    def __unicode__(self):
        return self.title

