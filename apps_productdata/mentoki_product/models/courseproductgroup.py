# coding: utf-8


"""
Courseevents are for sale. This app handles the public data
of coruseevents
"""

from __future__ import unicode_literals, absolute_import

import datetime

from django.db import models

from django.utils.translation import ugettext_lazy as _

import logging
logger = logging.getLogger(__name__)

from froala_editor.fields import FroalaField

from model_utils import Choices
from model_utils.models import TimeStampedModel

from apps_data.courseevent.models.courseevent import CourseEvent
from apps_data.course.models.course import Course

from .baseproduct import BaseProduct


class CourseProductGroupManager(models.Manager):
    """
    Querysets for CourseEvents
    """
    def by_mentor(self, user):
        return self.filter(course__courseowner__user=user).select_related('course')

    def published(self):
        return self.filter(published=True).select_related('course')


def foto_location(instance, filename):
        """
        location where the teachers foto is stored
        IN: CourseOwner, filename
        RETURN: path <course-slug>/<filename>
        """
        title = instance.course.title
        path = '/'.join([title, filename])
        logger.info("""[%s] [filename %s]:
                    Foto gespeichert unter %s"""
                    % (title,  filename, path))
        return path


class CourseProductGroup(TimeStampedModel):

    course = models.OneToOneField(Course)
    foto = models.ImageField(
        verbose_name=_('Foto'),
        help_text=_('''Hier kannst Du ein Foto für Deinen Kurs hochladen.'''),
        upload_to=foto_location, blank=True
    )
    in_one_sentence = models.CharField(
        verbose_name=_("in einem Satz"),
        help_text=_('beschreibe den Kurs in einem Satz'),
        max_length=250)

    published = models.BooleanField(default=True)

    slug = models.SlugField(default="x")
    title = models.CharField(max_length=100, default="x")
    conditions = FroalaField()
    about = FroalaField()
    mentors = FroalaField()
    discount_text = models.CharField(max_length=100, blank=True, default="")
    discount_text_long = models.CharField(max_length=200, blank=True, default="")

    objects = CourseProductGroupManager()

    class Meta:
        verbose_name = _("Kursproduktgruppen")
        verbose_name_plural = _("Kursproduktgruppen")

    def __unicode__(self):
        return self.course.title