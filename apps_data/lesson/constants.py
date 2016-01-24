# coding: utf-8

"""
Lessons Type
"""
from __future__ import unicode_literals, absolute_import

from django.utils.translation import ugettext_lazy as _

from django_enumfield import enum


class LessonType(enum.Enum):
    """
    Eventually in the future there will be more states, like the reason
    why the customer cannot buy the product.
    """
    ROOT = 0
    BLOCK = 1
    LESSON = 2
    LESSONSTEP = 3

    labels = {
        ROOT: _('Wurzel'),
        BLOCK: _('Block'),
        LESSON: _('Lektion'),
        LESSONSTEP:_('Lernabschnitt')
    }
