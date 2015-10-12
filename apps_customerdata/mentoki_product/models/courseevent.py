# coding: utf-8


"""
Courseevents are for sale. This app handles the public data
of coruseevents
"""

from __future__ import unicode_literals, absolute_import

import datetime

from django.db import models

from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel

from model_utils import Choices

import logging
logger = logging.getLogger(__name__)

#from django_prices.models import PriceField

from froala_editor.fields import FroalaField

from apps_data.courseevent.models.courseevent import CourseEvent

from .base import BaseProduct


class CourseEventProductManager(models.Manager):
    """
    Querysets for CourseEvents
    """
    def courseevents_for_sale(self):
        return CourseEventProduct.objects.all().select_related('courseevent')


def foto_location(instance, filename):
        """
        location where the teachers foto is stored
        IN: CourseOwner, filename
        RETURN: path <course-slug>/<filename>
        """
        title = instance.courseevent.course.title
        path = '/'.join([title, filename])
        logger.info("""[%s] [filename %s]:
                    Foto gespeichert unter %s"""
                    % (title,  filename, path))
        return path

class CourseEventProduct(BaseProduct):

    courseevent = models.OneToOneField(
        CourseEvent,
        on_delete=models.PROTECT
    )
    foto = models.ImageField(
        verbose_name=_('Foto'),
        help_text=_('''Hier kannst Du ein Foto für Deinen Kurs hochladen.'''),
        upload_to=foto_location, blank=True
    )
    in_one_sentence = models.CharField(
        verbose_name=_("in einem Satz"),
        help_text=_('beschreibe den Kurs in einem Satz'),
        max_length=250)
    format = models.CharField(
        verbose_name=_("Kursformart kurz"),
        max_length=250,
        blank=True)
    duration = models.CharField(
        verbose_name=_("Kursdauer"),
        max_length=250,
        blank=True)
    agb = FroalaField()

    objects = CourseEventProductManager()

    class Meta:
        verbose_name = _("Kursereignisverkauf")
        verbose_name_plural = _("Kursereignisverkäufe")

    def __unicode__(self):
        return self.courseevent.title


