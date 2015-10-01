# coding: utf-8


"""
Courseevents are for sale. This app handles the public data
of coruseevents
"""

from __future__ import unicode_literals, absolute_import

import datetime

from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import get_object_or_404
from django.core.validators import ValidationError

from model_utils.models import TimeStampedModel
from model_utils.managers import QueryManager
from model_utils.fields import MonitorField
from model_utils import Choices

import logging
logger = logging.getLogger(__name__)

#from django_prices.models import PriceField

from apps_data.courseevent.models.courseevent import CourseEvent


class CourseEventProductManager(models.Manager):
    """
    Querysets for CourseEvents
    """
    pass


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

class CourseEventProduct(TimeStampedModel):

    courseevent = models.OneToOneField(
        CourseEvent,
        on_delete=models.PROTECT
    )
    PRICEMODEL = Choices(('0', 'regular', _('regulär')),
                        ('1', 'gutschein', _('Gutscheine')),
                        ('a', 'empfehlung', _('Empfehlung'))
                             )
    pricemodel =  models.CharField(
        verbose_name="interner Status",
        max_length=2,
        choices=PRICEMODEL,
        default=PRICEMODEL.regular)

    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name=_('Preis')
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
    format_card = models.CharField(
        verbose_name=_("Kursformart kurz"),
        max_length=250,
        blank=True)
    objects = CourseEventProductManager()

    class Meta:
        verbose_name = _("Kursereignisverkauf")
        verbose_name_plural = _("Kursereignisverkäufe")

    def __unicode__(self):
        return self.courseevent.title


