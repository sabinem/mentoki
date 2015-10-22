#encoding: utf-8

import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _

from .customer import Customer
from apps_productdata.mentoki_product.models.courseproduct import CourseProduct


class TransactionManager(models.Manager):
    def create(self, amount, currency,
               product, customer,
               braintree_merchant_account_id,
               braintree_transaction_id):
        transaction = Transaction(
            amount=amount,
            currency=currency,
            product=product,
            customer=customer,
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
    courseproduct = models.ForeignKey(
        CourseProduct,
        blank=True,
        null=True
    )
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

    objects = TransactionManager()

    class Meta:
        verbose_name = 'Transaktion'
        verbose_name_plural = 'Transaktionen'

    def __unicode__(self):
        return self.braintree_transaction_id




