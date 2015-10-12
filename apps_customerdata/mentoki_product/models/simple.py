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

#from django_prices.models import PriceField

from froala_editor.fields import FroalaField

from apps_data.courseevent.models.courseevent import CourseEvent

from .base import BaseProduct


class SimpleProductManager(models.Manager):
    """
    Querysets for CourseEvents
    """
    pass

class SimpleProduct(BaseProduct):
    pass

    objects = SimpleProductManager()

    class Meta:
        verbose_name = _("Produk")
        verbose_name_plural = _("Produkte")

    def __unicode__(self):
        return self.name


