# coding: utf-8


"""
Courseevents are for sale. This app handles the public data
of coruseevents
"""

from __future__ import unicode_literals, absolute_import

from django.db import models

from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel

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

    netto_vk = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name=_('Netto Preis')
    )
    mwst = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name=_('Mehrwertsteuer')
    )
    mentoki_netto = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name=_('Mentoki Provision netto')
    )
    mentoki_mwst = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name=_('Mentoki Mehrwertsteuer')
    )
    price_total = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name=_('Verkaufspreis'))
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

    #def price_total(self):
    #    total = 0
    #    if self.netto_vk:
    #        total += self.netto_vk
    #    if self.mentoki_netto:
    #        total += self.mentoki_netto
    #    if self.mwst:
    #        total += self.mwst
    #    if self.mentoki_mwst:
    #        total += self.mentoki_mwst
    #
    #    return total

    def price_paymill(self):
        return self.price_total() * 100
