# coding: utf-8

"""
Choices for
 1. orders status
 2. transaction error codes
"""
from __future__ import unicode_literals, absolute_import

from django.utils.translation import ugettext_lazy as _

from django_enumfield import enum


class StartDesk(enum.Enum):
    """
    Eventually in the future there will be more states, like the reason
    why the customer cannot buy the product.
    """
    INITIAL = 0
    LEARN = 1
    TEACH = 2
    ACCOUNT = 3
    PROFILE = 4

    labels = {
        INITIAL: _('Start'),
        LEARN: _('Kurse zum Lernen'),
        TEACH: _('Eigener Unterricht'),
        ACCOUNT: _('Buchungsübersicht'),
        PROFILE: _('Profildaten')
    }
