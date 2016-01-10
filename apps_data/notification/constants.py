# coding: utf-8

"""
Choices for
 1. orders status
 2. transaction error codes
"""
from __future__ import unicode_literals, absolute_import

from django.utils.translation import ugettext_lazy as _

from django_enumfield import enum


class NotificationType(enum.Enum):
    """
    Eventually in the future there will be more states, like the reason
    why the customer cannot buy the product.
    """
    THREAD_CREATED = 1
    POST_CREATED = 2
    ANNOUNCEMENT = 3

    labels = {
        THREAD_CREATED: _('neuer Beitrag'),
        POST_CREATED: _('neuer Post'),
        ANNOUNCEMENT: _('Ankündingung'),
    }
