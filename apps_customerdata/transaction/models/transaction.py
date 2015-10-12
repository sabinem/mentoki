#encoding: utf-8

import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps_customerdata.customer.models import Customer
from apps_customerdata.mentoki_product.models.courseevent import CourseEventProduct


class TransactionManager(models.Manager):
    def create(self, amount, currency,
               product, customer,
               braintree_merchant_account_id, braintree_customer_id,
               braintree_transaction_id):
        transaction = Transaction(
            amount=amount,
            currency=currency,
            product=product,
            customer=customer,
            braintree_customer_id=braintree_customer_id,
            braintree_merchant_account_id=braintree_merchant_account_id,
            braintree_transaction_id=braintree_transaction_id)
        transaction.save()
        return transaction

class Transaction(models.Model):
    """
    This is an abstract class that defines a structure of Payment model that will be
    generated dynamically with one additional field: ``order``
    """
    # what mentoki wanted
    amount = models.DecimalField(
        _("amount"),
        decimal_places=4,
        max_digits=20)
    currency = models.CharField(
        _("currency"),
        default='USD',
        max_length=3)
    product = models.ForeignKey(CourseEventProduct)
    customer = models.ForeignKey(Customer)
    # what braintree got
    braintree_transaction_id = models.CharField(
        max_length=50,
        primary_key=True,
        default="x")
    braintree_customer_id = models.CharField(
        'braintree_customer_id',
        max_length=36,
        default="x")
    braintree_merchant_account_id = models.CharField(
        'braintree_merchant',
        max_length=100,
        default="default")
    created = models.DateTimeField(auto_now_add=True)

    objects = TransactionManager()

    def __unicode__(self):
        return self.braintree_transaction_id





