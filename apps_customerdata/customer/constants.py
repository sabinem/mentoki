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
    VALID = 1
    CANCELED = 10
    REFUNDED = 11

    labels = {
        INITIAL: _('angelegt'),
        VALID: _('gültig'),
        CANCELED: _('abgesagt'),
        REFUNDED: _('zurückerstattet, nach einer Absage'),
    }


class ContactReason(enum.Enum):
    """
    Eventually in the future there will be more states, like the reason
    why the customer cannot buy the product.
    """
    TEACH = 0
    LEARN = 1
    STARTERCOURSE = 10
    OTHER = 11

    labels = {
        TEACH: _('ich möchte unterrichten'),
        LEARN: _('ich interessiere mich für einen Kurs'),
        STARTERCOURSE: _('Ich interessiere mich für den Mentoki Starterkurs'),
        OTHER: _('es geht um etwas anderes'),
    }