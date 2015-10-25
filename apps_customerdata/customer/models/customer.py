# coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.db import models
from django.conf import settings

from model_utils.models import TimeStampedModel

from apps_productdata.mentoki_product.models.courseproduct import CourseProduct
#from apps_customerdata.customer.models.order import Order


class CustomerManager(models.Manager):
    """
    Manager for customers
    """
    def create_new_customer(
            self,
            braintree_customer_id,
            first_name,
            last_name,
            email,
            user):
        customer = Customer(
            braintree_customer_id=braintree_customer_id,
            first_name=first_name,
            last_name=last_name,
            email=email,
            user=user
        )
        customer.save()
        return customer


class Customer(TimeStampedModel):
    """
    Customer: stores connection to braintree object as braintree_customer_id
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

    email = models.EmailField(
        'Kundenemail'
    )

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

    def purchased_products(self, course):
        return CourseProduct.objects.filter(order__customer=self, course=course).order_by('display_nr')

    def purchased_products_ids(self, course):
        return self.purchased_products(course=course).values_list('pk', flat=True)

    def available_products(self, course):
        purchased = self.purchased_products_ids(course=course)
        independent = CourseProduct.objects.filter(course=course, has_dependencies=False).\
            exclude(id__in=purchased)
        dependent = CourseProduct.objects.filter(course=course, has_dependencies=True).\
            filter(dependencies=purchased).exclude(id__in=purchased)
        available = dependent | independent
        available.order_by('display_nr')
        return available

    def available_products_ids(self, course):
        return self.available_products(course=course).values_list('pk', flat=True)

    def not_yet_avalable(self, course):
        return CourseProduct.objects.filter(course=course, has_dependencies=True,
                                            id__in=self.available_products_ids(course)).order_by('display_nr')

