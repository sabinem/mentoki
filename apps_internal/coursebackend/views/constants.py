# coding: utf-8

"""
Choices for
 1. Action Code for Courseevent in the Backend: close and open classroom,
    hide or unhide in the menu
"""
from __future__ import unicode_literals, absolute_import

from django.utils.translation import ugettext_lazy as _

from django_enumfield import enum


class AlterCourseEvent(enum.Enum):
    """
    Eventually in the future there will be more states, like the reason
    why the customer cannot buy the product.
    """
    OPEN = 0
    CLOSE = 1
    HIDE = 2
    UNHIDE = 3

    labels = {
        OPEN: _('Klassenzimmer öffnen'),
        CLOSE: _('Klassenzimmer schliessen'),
        HIDE: _('verstecken'),
        UNHIDE: _('zeigen'),
    }