# coding: utf-8

"""
Choices for currency
"""
from django.utils.translation import ugettext_lazy as _

from model_utils import Choices

CURRENCY_CHOICES = Choices(
    ('EUR', 'euro',_('Euro')),
    ('CHF', 'chf',_('Schweizer Franken')),
)
