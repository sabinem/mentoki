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

    def create(self, braintree_customer_id, first_name, last_name, email, user=None, authenticated_user=False):
        customer = Customer(first_name=first_name, last_name=last_name, email=email,
                      braintree_customer_id=braintree_customer_id )
        if authenticated_user:
            customer.user = user
        customer.save()
        return customer

class Customer(TimeStampedModel):
    """
    An example customer model.
    Should store the shipping and billing address(es).
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name='customer',
        blank=True,
        null=True
    )
    braintree_customer_id = models.CharField(
        'braintree_customer_id',
        max_length=36,
        primary_key=True
        )

    email = models.EmailField()

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Kunde'
        verbose_name_plural = 'Kunden'

    objects = CustomerManager()

    def __unicode__(self):
        return 'Customer: %s %s %s : %s' \
               % (self.braintree_customer_id,
                  self.first_name,
                  self.last_name,
                  self.user,)
