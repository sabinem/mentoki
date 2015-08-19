# coding: utf-8
from __future__ import unicode_literals, absolute_import
# import from python
import datetime
# import from django
from django.db import models
from django.contrib.auth.models import User
# import from third party
from model_utils.models import TimeStampedModel
# import from other apps
from apps_data.course.models.oldcoursepart import Course, CourseUnit

from .courseevent import CourseEvent
from django.core.urlresolvers import reverse
from django.utils.functional import cached_property



class CourseeventUnitPublish(models.Model):
    """
    Units (Lessons) are published in a class, when the instructor decides
    students are ready for them. Publication is decided on the level of the
    CourseUnit. See app course for details.
    """
    courseevent = models.ForeignKey(CourseEvent)
    unit = models.ForeignKey(CourseUnit)
    published_at_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s / %s' % (self.courseevent, self.unit)

    class Meta:
        verbose_name = "XUnitPublish"


#old will be deleted after data have bben transeferred
class CourseEventPubicInformation(TimeStampedModel):
    """
    Decribing Attributes that are not necessary for processing them are gathered in this model
    """
    # should I make tis a one-to-one field?
    courseevent = models.ForeignKey(CourseEvent)
    # the video is shown in a certain way, therefor just the code of the video is needed here.
    video_url = models.CharField(max_length=100, blank=True, verbose_name="Kürzel des Videos bei You Tube ")
    text = models.TextField(blank=True, verbose_name="freie Kursbeschreibung")
    format = models.TextField(blank=True, verbose_name="Kursformat")
    workload = models.TextField(blank=True, verbose_name="Arbeitsbelastung")
    project = models.TextField(blank=True,  verbose_name="Teilnehmernutzen")
    structure = models.TextField(blank=True,  verbose_name="Gliederung")
    target_group = models.TextField(blank=True, verbose_name="Zielgruppe")
    prerequisites = models.TextField(blank=True, verbose_name="Voraussetzungen")

    def __unicode__(self):
        return u'%s' % (self.courseevent)

    def get_absolute_url(self):
        return CourseEvent.get_absolute_url(self.courseevent)

    class Meta:
        verbose_name = "XCourseeventInfo"