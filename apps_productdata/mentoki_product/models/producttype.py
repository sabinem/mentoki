# coding: utf-8


"""
Courseevents are for sale. This app handles the public data
of coruseevents
"""

from __future__ import unicode_literals, absolute_import

from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel
from model_utils.fields import MonitorField
from model_utils import Choices

from apps_data.courseevent.models.courseevent import CourseEvent
from apps_data.course.models.course import Course

from froala_editor.fields import FroalaField

from ..constants import CURRENCY_CHOICES

import logging
logger = logging.getLogger(__name__)


class ProductTypeManager(models.Manager):
    """
    Querysets for CourseEvents
    """
    pass

class ProductType(models.Model):

    name = models.CharField(max_length=200, default="Kurs")
    description = models.TextField()
    is_part = models.BooleanField()
    is_test = models.BooleanField()
    belongs_to_course = models.BooleanField()
    is_courseevent_participation = models.BooleanField()
    can_be_bought_only_once = models.BooleanField(default=False)
    has_dependencies = models.BooleanField(default=False)

    objects = ProductTypeManager()

    class Meta:
        verbose_name = _("Produktart")
        verbose_name_plural = _("Produktarten")

    def __unicode__(self):
        return "%s" % (self.name)
