# coding: utf-8

"""
The ordermodel processes bookings of courseproducts
"""

from __future__ import unicode_literals, absolute_import

from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel

from apps_productdata.mentoki_product.models.courseproduct import CourseProduct
from apps_customerdata.customer.models.customer import Customer
from apps_data.course.models.course import Course
from apps_productdata.mentoki_product.constants import Currency
from ..constants import OrderStatus
from django_enumfield import enum


import logging
logger = logging.getLogger(__name__)


class OrderManager(models.Manager):
    """
    Products that Mentoki sells
    """
    def products_with_order_paid_for_course_and_customer(self,
            course,
            customer):
        product_ids = self.filter(
            customer=customer,
            order_status=OrderStatus.PAID,
            course=course).\
            values_list('courseproduct', flat=True)
        return CourseProduct.objects.filter(id__in=product_ids)

    def by_customer(self, customer):
        return self.filter(customer=customer)


class Order(TimeStampedModel):
    """
    Order of a product: the order contains the product data, a timestamp
    and the participant data. It includes the participant username in case
    of unregistered users, that will be registered automatically once the
    order was processed.
    """
    courseproduct = models.ForeignKey(CourseProduct, blank=True, null=True)

    # for new users the customer is not set when the order is created
    customer = models.ForeignKey(
        Customer,
        related_name="Kunde",
        verbose_name=_('Kunde, Teilnehmer, der gebucht hat'),
        blank=True,
        null=True)

    # the course is part of the order since it may serve as an index
    course = models.ForeignKey(Course, blank=True, null=True)

    # "user" data, at the point of time when the order was taken
    # these belong to the participant that will be later logged in
    email = models.EmailField(
        _('Email des Teilnehmers'),
         default="x"
    )
    first_name = models.CharField(
        _('Vorname der Teilnehmers'),
        default="x",
        max_length=40)
    last_name = models.CharField(
        max_length=40,
        default="x"
    )

    # transaction status
    order_status = enum.EnumField(
        OrderStatus,
        default=OrderStatus.INITIAL
    )
    # amount and currency that was paid
    amount = models.DecimalField(
        _("Betrag"),
        decimal_places=4,
        max_digits=20,
        default=0
    )
    #currency = enum.EnumField(
    #    Currency,
    #    default=Currency.EUR)


    objects = OrderManager()

    class Meta:
        unique_together=('customer', 'courseproduct')
        verbose_name = 'Buchung'
        verbose_name_plural = 'Buchungen'

    def __unicode__(self):
        return 'Order: [%s: %s] ' \
               % (self.customer, self.courseproduct)

    def __repr__(self):
        return '[%s] %s %s' \
               % (self.id, self.customer, self.courseproduct)

    def save(self, **kwargs):
        self.course = self.courseproduct.course
        super(Order, self).save()
