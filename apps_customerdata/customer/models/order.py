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
from model_utils import Choices

from apps_productdata.mentoki_product.models.courseproduct import CourseProduct
from apps_customerdata.customer.models.customer import Customer
from django.conf import settings
from apps_customerdata.customer.models.transaction import Transaction


import logging
logger = logging.getLogger(__name__)


class BaseProductManager(models.Manager):
    """
    Products that Mentoki sells
    """
    def by_customer(self,customer):
        return self.filter(customer=customer)


class Order(TimeStampedModel):

    order_type = models.CharField(max_length=200, default="Kurs-Teilnahme")

    courseproduct = models.ForeignKey(CourseProduct, blank=True, null=True)
    customer = models.ForeignKey(
        Customer,
        'Kunde, der bezahlt hat'                         ,
        blank=True,
        null=True )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        'Teilnehmer als Benutzer'
    )
    participant_email=models.EmailField(
        'Email des Teilnehmers'
    )
    is_paid = models.BooleanField(default=True)
    transaction = models.ManyToManyField(Transaction)

    definitive = models.BooleanField()
    ORDER_STATUS = Choices(
        ('booked', 'booked',_('Gebucht')),
        ('confirmed', 'confirmed',_('Bestätigt')),
    )
    order_status = models.CharField( max_length=12, choices=ORDER_STATUS,
                                 default=ORDER_STATUS.booked )


