# coding: utf-8

"""
Choices for
 1. orders status
 2. transaction error codes
"""
from __future__ import unicode_literals, absolute_import

from django.utils.translation import ugettext_lazy as _

from model_utils import Choices

ORDER_STATUS = Choices(
    ('initial', 'initial',_('aufgenommen')), # initial order before transaction
    ('paid', 'paid',_('bezahlt')), # order has been paid
    ('failed', 'payment_failed',_('Zahlung fehlgeschlagen')), # payment declined
    ('error', 'payment_error',_('Zahlungsfehler')), #payment error on our side
    ('canceled', 'canceled',_('storniert')), #cancelled
    ('refunded', 'refunded',_('zurückerstattet')), # refundend
)

ORDER_STATUS_UNPAID = [ORDER_STATUS.initial,
                       ORDER_STATUS.payment_failed,
                       ORDER_STATUS.payment_error]

ORDER_STATUS_PAID = [ORDER_STATUS.paid]


TRANSACTION_ERROR_CODE = Choices(
    ('already_paid', 'already_paid',_('Order wurde bereits bezahlt.')),
                     # order has already been paid
)
