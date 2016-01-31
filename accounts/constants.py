# coding: utf-8

"""
Choices for
 1. notification settings
"""
from __future__ import unicode_literals, absolute_import

from django.utils.translation import ugettext_lazy as _

from django_enumfield import enum


# coding: utf-8


class NotificationSetting(enum.Enum):
    """
    Eventually in the future there will be more states, like the reason
    why the customer cannot buy the product.
    """
    SHOW_NOTIFICATIONS = 1
    SEND_EMAIL = 2
    BOTH = 3

    labels = {
        SHOW_NOTIFICATIONS: _('nur Nachrichten'),
        SEND_EMAIL: _('nur Emails'),
        BOTH: _('beides: emails und Nachrichten'),
    }
