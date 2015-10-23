# coding: utf-8


"""
Courseevents are for sale. This app handles the public data
of coruseevents
"""

from __future__ import unicode_literals, absolute_import

from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel
from model_utils import Choices

from apps_productdata.mentoki_product.models.courseproduct import CourseProduct
from apps_customerdata.customer.models.customer import Customer
from apps_data.course.models.course import Course
from apps_productdata.mentoki_product.constants import CURRENCY_CHOICES


import logging
logger = logging.getLogger(__name__)


class OrderManager(models.Manager):
    """
    Products that Mentoki sells
    """
    def by_customer(self,customer, income, currency):
        return self.filter(customer=customer)

    def create(self, courseproduct, customer, income, currency):
        order = Order(
            courseproduct=courseproduct,
            customer=customer,
            income=income,
            currency=currency,
            course=courseproduct.course
            )

        order.save()
        y=x
        return order


class Order(TimeStampedModel):
    """
    Order of a product
    """
    courseproduct = models.ForeignKey(CourseProduct, blank=True, null=True)
    customer = models.ForeignKey(
        Customer,
        verbose_name='Kunde, der bezahlt hat',
        blank=True,
        null=True )
    course = models.ForeignKey(Course, blank=True, null=True)
    ORDER_STATUS = Choices(
        ('fix', 'fix',_('Nicht mehr erstattbar')),
        ('paid', 'paid',_('bezahlt')),
        ('canceled', 'canceled',_('storniert')),
        ('refunded', 'refunded',_('zurückerstattet')),
    )
    order_status = models.CharField( max_length=12, choices=ORDER_STATUS,
                                 default=ORDER_STATUS.paid )
    income = models.DecimalField(
        _("amount"),
        decimal_places=4,
        max_digits=20,
        default=0
    )
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES,
        default=CURRENCY_CHOICES.euro )



