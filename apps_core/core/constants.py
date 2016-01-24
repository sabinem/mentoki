# coding: utf-8

"""
CRUD Operation
"""
from __future__ import unicode_literals, absolute_import

from django.utils.translation import ugettext_lazy as _

from django_enumfield import enum


# coding: utf-8


class CRUDOperation(enum.Enum):
    """
    Eventually in the future there will be more states, like the reason
    why the customer cannot buy the product.
    """
    LIST = 0
    DETAIL = 1
    UPDATE = 2
    INSERT = 3
    DELETE = 4

    labels = {
        LIST: _('Liste von Objekten'),
        DETAIL: _('Objekt ansehen'),
        UPDATE: _('Objekt ändern'),
        INSERT: _('Objekt einfügen'),
        DELETE: _('Objekt löschen'),
    }
