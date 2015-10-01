# coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.conf import settings
from django.db import models

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

class Customer(TimeStampedModel):
    """
    An example customer model.
    Should store the shipping and billing address(es).
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name='customer',
        primary_key=True,
    )
    id = models.CharField(
        verbose_name='Kunden-Nr.',
        max_length=36,
        unique=True)
    street = models.CharField(
        verbose_name='Strasse',
        max_length=100, default="x")
    house_nr = models.CharField(
        verbose_name='Hausnummer',
        max_length=100, default=1)
    town = models.CharField(
        verbose_name='Stadt',
        max_length=100, default="x")
    plz = models.CharField(
        verbose_name='Postleitzahl',
        max_length=5, default=1) ,
    country = models.CharField(
        verbose_name='Land',
        default='de',
        max_length=100
    )

    class Meta:
        verbose_name = 'customer'
        verbose_name_plural = 'customers'

    def __unicode__(self):
        return 'Customer: %s' % self.user
