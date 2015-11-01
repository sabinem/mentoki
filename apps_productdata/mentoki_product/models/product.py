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

from froala_editor.fields import FroalaField

from ..constants import CURRENCY_CHOICES
from .producttype import ProductType

import logging
logger = logging.getLogger(__name__)


class ProductManager(models.Manager):
    """
    Querysets for CourseEvents
    """
    pass

class Product(TimeStampedModel):

    name = models.CharField(max_length=200, default="Kurs-Teilnahme")

    description = FroalaField()

    # for braintree, invoices, etc.
    invoice_descriptor = models.CharField(max_length=250, default="x")

    # price with currency
    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name=_('Verkaufspreis'))
    currency = models.CharField(
        max_length=3,
        choices=CURRENCY_CHOICES,
        default=CURRENCY_CHOICES.euro)
    price_changed = MonitorField(
                monitor='price',
                verbose_name=_("letzte Preisänderung am"))

    # for display: each product has its own product page
    slug = models.SlugField()
    display_nr = models.IntegerField(default=1)

    # for search engines
    meta_keywords = models.CharField(max_length=200, default="x")
    meta_description = models.CharField(max_length=200, default="x")
    meta_title = models.CharField(max_length=100, default="x")

    product_type = models.ForeignKey(
        ProductType,
        verbose_name="Produktart",
    )

    objects = ProductManager()

    class Meta:
        abstract = True

    def __unicode__(self):
        return "%s: %s" % (self.name)








