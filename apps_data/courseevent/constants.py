# coding: utf-8

"""
Choices for currency: so far there are CHF and EUR

Choice for the reach of an offer: doese it apply to the whole course
    or just to an event or only to a product
"""
from django.utils.translation import ugettext_lazy as _

from model_utils import Choices

PARTICIPANT_STATUS_CHOICES = Choices(
    ('preview', 'preview',_('Feedbackgeber')),
    ('full', 'full',_('komplett')),
    ('part', 'part',_('Teile gebucht')),
)

