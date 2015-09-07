# coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.conf import settings
from django.db import models


class Customer(models.Model):
    """
    An example customer model.
    Should store the shipping and billing address(es).
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name='customer',
        primary_key=True,
    )
    id = models.CharField('customer', max_length=36, unique=True)


    class Meta:
        verbose_name = 'customer'
        verbose_name_plural = 'customers'

    def __unicode__(self):
        return 'Customer: %s' % self.user
