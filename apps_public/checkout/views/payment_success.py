# coding: utf-8

"""
Braintree Integration Payment Form
"""

from __future__ import unicode_literals, absolute_import

from django.shortcuts import get_object_or_404
from django.views.generic import FormView, TemplateView

from apps_productdata.mentoki_product.models.courseproduct import \
    CourseProduct
from apps_productdata.mentoki_product.models.courseproductgroup import \
    CourseProductGroup
from apps_customerdata.customer.models.transaction import SuccessfulTransaction

import logging
logger = logging.getLogger(__name__)


class SuccessView(
    TemplateView):
    """
    This view is called if the payment has been successful.
    """
    template_name = 'checkout/pages/payment_sucessful.html'

    def get_context_data(self, **kwargs):
        """
        gets the product and the braintree client token
        """
        context = super(SuccessView, self).get_context_data(**kwargs)

        context['transaction'] = get_object_or_404(
            SuccessfulTransaction,
            pk=self.kwargs['pk'])

        courseproduct = get_object_or_404(CourseProduct, slug=self.kwargs['slug'])
        context['courseproduct'] = courseproduct
        context['courseproductgroup'] = get_object_or_404(CourseProductGroup,
                                               course=courseproduct.course)
        return context