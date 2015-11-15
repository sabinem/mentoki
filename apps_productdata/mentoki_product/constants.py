# coding: utf-8

from enum import Enum

"""
Choices for currency: so far there are CHF and EUR

Choice for the reach of an offer: doese it apply to the whole course
    or just to an event or only to a product
"""
from django.utils.translation import ugettext_lazy as _
from django_enumfield import enum


class Currency(enum.Enum):
    EUR = 1
    CHF = 2

    labels = {
        EUR: _('EUR'),
        CHF: _('CHF')
    }

class Offerreach(enum.Enum):
    """
    Eventually in the future the reach will be expanded to be specific to
    a courseevent or to a product
    """
    PRODUCTGROUP = 1
    PRODUCTSUBGROUP = 2
    PRODUCT = 3

    labels = {
        PRODUCTGROUP:
            _('Kursgruppe'),
        PRODUCTSUBGROUP:
            _('Kursuntergruppe'),
        PRODUCT:
            _('EinzelProdukt'),
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

class Producttype(enum.Enum):
    """
    Eventually in the future there will be more states, like the reason
    why the customer cannot buy the product.
    """
    COURSEEVENT_TIMED = 1
    COURSEEVENT_DIRECT_ACCESS = 2
    COURSEEVENT_PART = 10
    OTHER = 20
    OTHER_EMAIL_ACCESSCODE = 21


    labels = {
        COURSEEVENT_TIMED: _('Kurseereignis mit Termin'),
        COURSEEVENT_DIRECT_ACCESS: _('Kursereignis mit direktem Zugang'),
        COURSEEVENT_PART: _('Teil eines Kursereignisses'),
        OTHER_EMAIL_ACCESSCODE: _('anderes mit Zugangscode'),
        OTHER: _('etwas anderes')
    }