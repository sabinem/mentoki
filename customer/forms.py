# coding: utf-8
""" Braintree Demo implementation
    https://developers.braintreepayments.com/javascript+python/start/hello-server
    Test credit card numbers:
    https://developers.braintreepayments.com/javascript+python/reference/general/testing
"""

from __future__ import unicode_literals, absolute_import
import braintree
from django.conf import settings
from django import forms
from django.core.urlresolvers import reverse
from django.views.generic import FormView, TemplateView
import logging
from .models import Customer

logger = logging.getLogger(__name__)


class BraintreeForm(forms.Form):
    first_name = forms.CharField(label='First name')
    last_name = forms.CharField(label='Last name')
    amount = forms.CharField(label='Amount')
    payment_method_nonce = forms.CharField()