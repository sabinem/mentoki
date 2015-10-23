#encoding: utf-8

import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _

from .customer import Customer
from apps_data.course.models.course import Course
from apps_customerdata.customer.models.order import Order
from apps_customerdata.customer.models.temporder import TempOrder
from apps_productdata.mentoki_product.constants import CURRENCY_CHOICES


class BaseTransaction(models.Model):
    """
    This is an abstract class that defines a structure of Payment model that will be
    generated dynamically with one additional field: ``order``
    """
    # what mentoki wanted
    amount = models.DecimalField(
        _("amount"),
        decimal_places=4,
        max_digits=20)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES,
        default=CURRENCY_CHOICES.euro )
    course = models.ForeignKey(Course, blank=True, null=True)
    customer = models.ForeignKey(Customer)
    # what braintree got
    braintree_transaction_id = models.CharField(
        max_length=50,
        primary_key=True,
        default="x")
    braintree_merchant_account_id = models.CharField(
        'braintree_merchant',
        max_length=100,
        default="default")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        verbose_name = 'Transaktion'
        verbose_name_plural = 'Transaktionen'

    def __unicode__(self):
        return self.braintree_transaction_id


class TransactionManager(models.Manager):
    def create(self, amount, currency,
               customer, order,
               braintree_merchant_account_id,
               braintree_transaction_id):
        transaction = SuccessfulTransaction(
            amount=amount,
            currency=currency,
            order=order,
            course=order.course,
            customer=customer,
            braintree_merchant_account_id=braintree_merchant_account_id,
            braintree_transaction_id=braintree_transaction_id)
        transaction.save()
        return transaction


class SuccessfulTransaction(BaseTransaction):
    """
    This is an abstract class that defines a structure of Payment model that will be
    generated dynamically with one additional field: ``order``
    """
    order = models.ForeignKey(
        Order
    )
    objects = TransactionManager()

    class Meta:
        verbose_name = 'Erfolgreiche Transaktion'
        verbose_name_plural = 'Erfolgreiche Transaktionen'

    def __unicode__(self):
        return self.braintree_transaction_id


class FailedTransactionManager(models.Manager):
    def create(self, amount, currency,
               customer, temporder,
               braintree_merchant_account_id,
               braintree_transaction_id):
        transaction = BaseTransaction(
            amount=amount,
            currency=currency,
            temporder = temporder,
            customer=customer,
            braintree_merchant_account_id=braintree_merchant_account_id,
            braintree_transaction_id=braintree_transaction_id)
        transaction.save()
        return transaction


class FailedTransaction(BaseTransaction):
    """
    This is an abstract class that defines a structure of Payment model that will be
    generated dynamically with one additional field: ``order``
    """
    # what mentoki wanted
    temporder = models.ForeignKey(
        TempOrder
    )
    braintree_result = models.TextField(blank=True)

    objects = FailedTransactionManager()

    class Meta:
        verbose_name = 'Nicht erfolgreiche Transaktion'
        verbose_name_plural = 'Nicht erfolgreiche Transaktionen'

    def __unicode__(self):
        return self.braintree_transaction_id