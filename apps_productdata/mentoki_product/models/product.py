# coding: utf-8

"""
Products are the items that are for sale on the mentoki site
"""

from __future__ import unicode_literals, absolute_import

from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel
from model_utils.fields import MonitorField

from froala_editor.fields import FroalaField

from ..constants import Currency, Producttype
from django_enumfield import enum

import logging
logger = logging.getLogger(__name__)


class ProductManager(models.Manager):
    """
    Querysets for Products
    """
    pass

class Product(TimeStampedModel):

    description = FroalaField()

    # price with currency
    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name=_('Verkaufspreis'))
    currency = enum.EnumField(Currency, default=Currency.EUR)
    price_changed = MonitorField(
                monitor='price',
                verbose_name=_("letzte Preisänderung am"))

    display_nr = models.IntegerField(default=1)

    # product type
    product_type = enum.EnumField(
        Producttype,
        default=Producttype.OTHER)

    objects = ProductManager()

    class Meta:
        abstract = True

    def __unicode__(self):
        return "%s: %s" % (self.name)








