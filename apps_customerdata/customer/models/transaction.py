# coding: utf-8

"""
Transactions are stored here. They correspond to braintree transactions.
"""

from __future__ import unicode_literals, absolute_import

from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel

from django_enumfield import enum

from apps_data.course.models.course import Course
from apps_customerdata.customer.models.order import Order
from apps_productdata.mentoki_product.constants import Currency

from ..constants import TransactionErrorCode
from .customer import Customer
from django_enumfield import enum


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
    order = models.ForeignKey(
        Order,
        verbose_name=_('Auftrag'),
    )

    # will be an index later on
    course = models.ForeignKey(
        Course,
        verbose_name=('Kurs'),
        blank=True,
        null=True
    )

    # customer that performs the transaction
    customer = models.ForeignKey(
        Customer,
        verbose_name=('Kunde'),
        blank=True,
        null=True
    )

    # payment intention
    amount = models.DecimalField(
        _('Betrag'),
        decimal_places=4,
        max_digits=20
    )
    currency = enum.EnumField(
        Currency,
        default=Currency.EUR,
        verbose_name=_('Währung'),
    )


    # "customer" data, at the point of time when the transaction happened
    email=models.EmailField(
        _('Email des Teilnehmers'),
        blank=True
    )
    first_name = models.CharField(
        _('Vorname der Teilnehmers'),
        blank=True,
        max_length=40
    )
    last_name = models.CharField(
        _('Nachname der Teilnehmers'),
        max_length=40,
        blank=True
    )

    # braintree transaction data and the merchant key that was used
    braintree_transaction_id = models.CharField(
        _('braintree Transaktionsnr.'),
        max_length=10,
        blank=True
    )
    braintree_customer_id = models.CharField(
        'braintree Kundennr.',
        max_length=10,
        blank=True
    )
    braintree_payment_token = models.CharField(
        'braintree Zahlunsmittel-Token.',
        max_length=10,
        blank=True
    )
    braintree_merchant_account_id = models.CharField(
        'braintree Merchant Accountnr.',
        max_length=20,
        blank=True
    )
    braintree_amount = models.CharField(
        _('braintree Betrag'),
        help_text=_('Was braintree abgebucht hat'),
        blank=True,
        max_length=10
    )

    # transaction status
    success = models.BooleanField(
        _('Flag ob die Transaktion erfolgreich war, insofern '
          'als tatsächlich bezahlt wurde.'),
        default=False
    )

    # eigener Fehlercode, der die Fehlerart grob anzeigt
    error_code = enum.EnumField(
        TransactionErrorCode,
        default=TransactionErrorCode.NO_ERROR,
    )
    # in case there was no success
    braintree_error_message = models.CharField(
        _('aus braintree Fehlernachricht: besetzt im Fehlerfall '),
        max_length=250,
        blank=True
    )
    braintree_error_details = models.TextField(
        _('aus braintree deep errors: besetzt im Fehlerfall '),
        blank=True
    )
    braintree_processor_response_code = models.CharField(
        _('Banken Processor Code: besetzt im Fehlerfall '),
        max_length=4,
        blank=True
    )
    braintree_processor_response_text = models.CharField(
        _('Banken Processor Text: besetzt im Fehlerfall '),
        max_length=250,
        blank=True,
    )

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
        return '[%s] %s' \
               % (self.id, self.course)

