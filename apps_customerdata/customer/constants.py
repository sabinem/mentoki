# coding: utf-8

"""
Choices for
 1. orders status
 2. transaction error codes
"""
from __future__ import unicode_literals, absolute_import

from django.utils.translation import ugettext_lazy as _

from django_enumfield import enum


class TransactionErrorCode(enum.Enum):
    """
    Eventually in the future there will be more states, like the reason
    why the customer cannot buy the product.
    """
    NO_ERROR = 0
    SUCCESS = 1
    TRY_TO_DOUBLE_PAY = 2
    BRAINTREE_CONNECTION_ERROR = 3

    FAILED_SYSTEMERROR = 4
    PAYMENT_DECLINED = 5

    labels = {
        NO_ERROR: _('Nicht gesetzt.'),
        SUCCESS: _('Erfolgreich'),
        BRAINTREE_CONNECTION_ERROR: _('Braintree Verbindungsfehler'),
        TRY_TO_DOUBLE_PAY: _('Die Buchung wurde bereits bezahlt'),
        PAYMENT_DECLINED: _('Zahlung abgelehnt '
                            'des Token aufgetreten.'),
        FAILED_SYSTEMERROR: _('Systemfehler'),
    }


class OrderStatus(enum.Enum):
    """
    Eventually in the future there will be more states, like the reason
    why the customer cannot buy the product.
    """
    INITIAL = 0
    PAID = 1
    UNPAID = 2
    CANCELED = 3
    REFUNDED = 4
    DECLINED = 5
    ERROR_DURING_PAYMENT = 6

    labels = {
        INITIAL: _('angelegt'),
        PAID: _('bezahlt'),
        UNPAID: _('bezahlung war nicht erfolgreich'),
        CANCELED: _('abgesagt'),
        REFUNDED: _('zurückerstattet, nach einer Absage'),
        DECLINED: _('Zahlung abgelehnt'),
        ERROR_DURING_PAYMENT: _('Fehler bei der Zahlung aufgetreten'),
    }

class PaymentErrorCode(enum.Enum):
    ORDER_ALREADY_PAID = 1
    BRAINTREE_ERROR = 2
    UNKNOWN_TOKEN_GENERATION_ERROR = 3

    labels = {
        ORDER_ALREADY_PAID: _('Der Kurs wurde bereits gebucht und bezahlt.'),
        BRAINTREE_ERROR: _('Fehler beim Verbindungsaufbau zu braintree.'),
    }