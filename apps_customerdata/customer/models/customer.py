# coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.db import models
from django.conf import settings

from model_utils.models import TimeStampedModel

from apps_productdata.mentoki_product.models.courseproduct import CourseProduct
from ..constants import ORDER_STATUS, ORDER_STATUS_UNPAID, ORDER_STATUS_PAID


class CustomerManager(models.Manager):
    """
    Manager for customers:
    """
    pass

class Customer(TimeStampedModel):
    """
    Customer: all users that have orders are considered
    customers. For payments a customer id from braintree is stored
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
        blank=True
        )

    class Meta:
        verbose_name = 'Kunde'
        verbose_name_plural = 'Kunden'

    objects = CustomerManager()

    #TODO: determine later
    def __unicode__(self):
        return 'Customer: %s' \
               % (self.user,)


