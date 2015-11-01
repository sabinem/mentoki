# coding: utf-8

"""
Braintree Integration Payment Form
"""

from __future__ import unicode_literals, absolute_import

from django.views.generic import TemplateView

import logging
logger = logging.getLogger(__name__)


class CheckoutFailedView(
    TemplateView):
    """
    This view handles failed checkout or payment in cases, where it
    does not make sense to continue
    """
    #TODO: decide on the context, what it should contein

    template_name = 'checkout/pages/checkout_failed.html'

    def get_context_data(self, **kwargs):
        """
        gets the product and the braintree client token
        """
        context = super(CheckoutFailedView, self).get_context_data(**kwargs)

        return context