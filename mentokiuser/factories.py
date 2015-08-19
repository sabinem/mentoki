# coding: utf-8

from __future__ import unicode_literals, absolute_import

from .models import Account

import factory

from .models import Account


class AccountFactory(factory.Factory):
    class Meta:
        model = Account

