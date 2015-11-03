#encoding: utf-8

"""
Transactions are stored here. They correspond to braintree transactions.
"""

from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel

from apps_data.course.models.course import Course
from apps_customerdata.customer.models.order import Order
from apps_productdata.mentoki_product.constants import CURRENCY_CHOICES

from ..constants import TRANSACTION_ERROR_CODE
from .customer import Customer


class TransactionManager(models.Manager):
    """
    handles Transactions with the payment provider braintree
    """
    pass


class Transaction(TimeStampedModel):
    """
    Transactions are stored in this model. A flag indicates whether
    they passed successfully.
    """
    # order must be present
    order = models.ForeignKey(Order)

    # will be an index later on
    course = models.ForeignKey(Course, blank=True, null=True)

    # customer that performs the transaction
    customer = models.ForeignKey(
        Customer,
        blank=True,
        null=True)

    # payment intention
    amount = models.DecimalField(
        _("amount"),
        decimal_places=4,
        max_digits=20)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES,
        default=CURRENCY_CHOICES.euro )

    # "customer" data, at the point of time when the transaction happened
    email=models.EmailField(
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

    # braintree transaction data and the merchant key that was used
    braintree_transaction_id = models.CharField(
        max_length=10,
        blank=True)
    braintree_customer_id = models.CharField(
        'braintree Kundennr.',
        max_length=10,
        blank=True)
    braintree_payment_token = models.CharField(
        'braintree Kundennr.',
        max_length=10,
        blank=True)
    braintree_merchant_account_id = models.CharField(
        'braintree_merchant',
        max_length=20,
        blank=True)
    braintree_amount = models.CharField(
        _("amount form braintree"),
        blank=True,
        max_length=10)

    # in case there was no success
    braintree_error_details = models.TextField(
        blank=True
    )

    # flag, whether the transaction had success
    flag_payment_sucess = models.BooleanField(default=False)

    # own error code
    error_code = models.CharField(
        max_length=12,
        choices=TRANSACTION_ERROR_CODE,
        blank=True,
        default="")
    # own error message
    error_message = models.CharField(
        max_length=250,
        blank=True,
        default="")

    objects = TransactionManager()

    class Meta:
        verbose_name = 'Transaktion'
        verbose_name_plural = 'Transaktionen'

    def __unicode__(self):
        return '[Auftrag %s][Transaktion %s] %s %s: %s %s' \
               % (self.order_id,
                  self.braintree_transaction_id,
                  self.first_name,
                  self.last_name,
                  self.amount,
                  self.currency)

    def __repr__(self):
        return '[%s] %s %s' \
               % (self.id, self.user, self.course)

