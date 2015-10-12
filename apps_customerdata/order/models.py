# coding: utf-8


"""
Courseevents are for sale. This app handles the public data
of coruseevents
"""

from __future__ import unicode_literals, absolute_import

from django.db import models
from django.conf import settings

from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel

from apps_customerdata.mentoki_product.models.courseevent import CourseEventProduct

#from.choices import CURRENCY_CHOICES

from model_utils import Choices


import logging
logger = logging.getLogger(__name__)


class BaseProductManager(models.Manager):
    """
    Products that Mentoki sells
    """
    pass


class Order(TimeStampedModel):

    name = models.CharField(max_length=200, default="Kurs-Teilnahme")

    product = models.ForeignKey(CourseEventProduct)
    customer = models.ForeignKey(settings.AUTH_USER_MODEL)
    payment_status = models.BooleanField()
