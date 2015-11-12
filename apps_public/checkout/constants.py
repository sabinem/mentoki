# coding: utf-8

from enum import Enum

"""
Error Codes for Payments
"""
from django.utils.translation import ugettext_lazy as _
from django_enumfield import enum


class PaymentErrorCode(enum.Enum):
    ORDER_ALREADY_PAID = 1
    BRAINTREE_AUTHORISATION_ERROR = 2
    UNKNOWN_TOKEN_GENERATION_ERROR = 3

    labels = {
        ORDER_ALREADY_PAID: _('Der Kurs wurde bereits gebucht und bezahlt.'),
        BRAINTREE_AUTHORISATION_ERROR: _('Der Zahlungsanbieter konnte nicht '
                                         'authorisiert werden.'),
        UNKNOWN_TOKEN_GENERATION_ERROR: _('Unbekannter Fehler beim Generieren '
                                         'des Token aufgetreten.' )
    }

class Offerreach(enum.Enum):
    """
    Eventually in the future the reach will be expanded to be specific to
    a courseevent or to a product
    """
    COURSE = 1

    labels = {
        COURSE: _('Das Angebot bezieht sich auf alle Produkte der Kursgruppe'),
    }

class ProductToCustomer(enum.Enum):
    """
    Eventually in the future there will be more states, like the reason
    why the customer cannot buy the product.
    """
    NOT_AVAILABLE = 0
    AVAILABLE = 1
    BOOKED = 2

    labels = {
        NOT_AVAILABLE: _('Der Kunde kann das Produkt nicht kaufen.'),
        AVAILABLE: _('Der Kunde kann das Produkt kaufen.'),
        BOOKED:_('Der Kunde hat das Produkt bereits gebucht')
    }


