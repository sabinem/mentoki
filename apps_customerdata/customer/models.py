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


class CustomerManager(models.Manager):

    def create(self, user, braintree_customer_id):
        customer = Customer(user=user,
                      braintree_customer_id=braintree_customer_id)
        customer.save()
        return customer

class Customer(TimeStampedModel):
    """
    An example customer model.
    Should store the shipping and billing address(es).
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name='customer'
    )
    braintree_customer_id = models.CharField(
        'braintree_customer_id',
        max_length=36,
        primary_key=True
        )


    class Meta:
        verbose_name = 'customer'
        verbose_name_plural = 'customers'

    objects = CustomerManager()

    def __unicode__(self):
        return 'Customer: %s' % self.user
