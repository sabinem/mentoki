# coding: utf-8

"""
Choices for currency: so far there are CHF and EUR

Choice for the reach of an offer: doese it apply to the whole course
    or just to an event or only to a product
"""
from django.utils.translation import ugettext_lazy as _

from model_utils import Choices

CURRENCY_CHOICES = Choices(
    ('EUR', 'euro',_('Euro')),
    ('CHF', 'chf',_('Schweizer Franken')),
)

OFFERREACH_CHOICES = Choices(
    ('course', 'course',_('course')),
    ('courseevent', 'courseevent',_('courseevent')),
    ('product', 'product',_('product')),
)


PRODUCT_TO_CUSTOMER_CASES = Choices(
    ('booked', 'booked',_('schon gebucht')),
    ('future', 'future',_('später buchbar')),
    ('never', 'never',_('nie buchbar')),
    ('now', 'now',_('jetzt buchbar')),
    ('undetermined', 'undetermined',_('unbestimmt')),
)