# coding: utf-8

"""
Choices for
 1. orders status
 2. transaction error codes
"""
from __future__ import unicode_literals, absolute_import

from django.utils.translation import ugettext_lazy as _

from model_utils import Choices


ORDER_ERROR_CODE = Choices(
    ('already_paid', 'already_paid',_('Order wurde bereits bezahlt.')),
)

BRAINTREE_ERROR_CODES = Choices(
    ('82670', 'creditcard_nr_invalid',_('Die Kreditkarten-Nr. ist ungültig')),
    ('93107', 'cannot_reuse_nounce',_('Die Authorisierung ist ungültig, '
                                      ' bitte die Seite nochmals laden.'))
)

