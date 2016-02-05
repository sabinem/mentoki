# coding: utf-8

"""
Choices for currency: so far there are CHF and EUR

Choice for the reach of an offer: doese it apply to the whole course
    or just to an event or only to a product
"""
from enum import Enum

from django.utils.translation import ugettext_lazy as _
from django_enumfield import enum


class MenuItemType(enum.Enum):
    HEADER = 0
    LESSON = 1
    FORUM = 2
    ANNOUNCEMENTS = 3
    PARTICIPANTS = 4

    labels = {
        HEADER: _('Überschrift'),
        LESSON: _('Lektion'),
        FORUM: _('Forum'),
        ANNOUNCEMENTS: _('Ankündigungsliste'),
        PARTICIPANTS: _('Teilnehmerliste')
    }


class FeedbackSpice(enum.Enum):
    MILD = 0
    MEDIUM = 1
    SPICY = 2

    labels = {
        MILD: _('mild'),
        MEDIUM: _('mittel'),
        SPICY: _('scharf'),
    }


class NotificationSettings(enum.Enum):
    NONE = 0
    PARTICIPATING = 1
    ALL = 2

    labels = {
        NONE: _('nie'),
        PARTICIPATING: _('nur wenn ich direkt beteiligt bin'),
        ALL: _('immer'),
    }