# coding: utf-8

"""
Transactions are stored here. They correspond to braintree transactions.
"""

from __future__ import unicode_literals, absolute_import

from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel

from apps_customerdata.customer.models.transaction import Transaction


class BraintreeLog(TimeStampedModel):
    """
    Transactions are stored in this model. A flag indicates whether
    they passed successfully.
    """
    # order must be present
    mentoki_transaction = models.ForeignKey(Transaction)
    transaction_data = models.TextField()
    result = models.BooleanField(default=False)

