# coding: utf-8

"""
Braintree Integration Payment Form
"""

from __future__ import unicode_literals, absolute_import

from django.shortcuts import get_object_or_404
from django.views.generic import FormView, TemplateView

from apps_public.storefront.views.info import CourseGroupMixin

import logging
logger = logging.getLogger(__name__)


class SuccessView(
    CourseGroupMixin,
    TemplateView):
    """
    This view is called if the payment has been successful.
    """
    template_name = 'courseoffer/pages/payment_sucessful.html'

    def get_context_data(self, **kwargs):
        """
        gets the product and the braintree client token
        """
        context = super(SuccessView, self).get_context_data(**kwargs)
        context['transaction'] = get_object_or_404(
            Transaction,
            pk=self.kwargs['pk'])
        return context