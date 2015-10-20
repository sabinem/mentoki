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

#from.choices import CURRENCY_CHOICES

from model_utils import Choices


import logging
logger = logging.getLogger(__name__)


class BaseProductManager(models.Manager):
    """
    Products that Mentoki sells
    """
    pass


class BaseProduct(TimeStampedModel):

    name = models.CharField(max_length=200, default="Kurs-Teilnahme")

    description = models.CharField(max_length=200, blank=True, default="Kurs-Teilnahme")

    product_nr = models.CharField(max_length=20, default=1)

    slug = models.SlugField(default="x")

    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True,
        default=0,
        verbose_name=_('Verkaufspreis'))
    price_changed = MonitorField(
            monitor='price',
            verbose_name=_("letzte Preisänderung am"))
    CURRENCY_CHOICES = Choices(
        ('EUR', 'euro',_('Euro')),
        ('CHF', 'chf',_('Schweizer Franken')),
    )
    currency = models.CharField( max_length=3, choices=CURRENCY_CHOICES,
                                 default=CURRENCY_CHOICES.euro )

    objects = BaseProductManager()

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        #TODO check wether prices addup to total price
        super(BaseProduct, self).save(*args, **kwargs)
