# coding: utf-8

"""
Braintree Integration Payment Form
"""

from __future__ import unicode_literals, absolute_import

from django.shortcuts import get_object_or_404
from django.views.generic import FormView, TemplateView
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth import login
from django.core.exceptions import ObjectDoesNotExist

from braces.views import MessageMixin

from braces.views import LoginRequiredMixin
from apps_core.email.utils.payment import send_receipt

from apps_productdata.mentoki_product.models.courseproduct import \
    CourseProduct
from apps_productdata.mentoki_product.models.courseproductgroup import \
    CourseProductGroup
from apps_customerdata.customer.models.order import Order
from apps_customerdata.customer.models.transaction import Transaction
from apps_data.courseevent.models.courseevent import CourseEventParticipation

import logging
logger = logging.getLogger('activity.payments')
logger_sentry = logging.getLogger('sentry.payments')


class PaymentSuccessView(
    TemplateView):
    """
    This view is called if the payment has been successful.
    The user has to be logged in for payment
    """
    template_name = 'checkout/pages/payment_sucessful.html'

    def get_context_data(self, **kwargs):
        """
        get order from the url kwargs
        """
        context = super(PaymentSuccessView, self).get_context_data(**kwargs)
        try:
            order = Order.objects.get(pk=self.kwargs['order_pk'])
            transaction = \
                Transaction.objects.get(pk=self.kwargs['transaction_pk'])
        except ObjectDoesNotExist:
            logger_sentry.error('Nach der Zahlung fehlten Transaction oder Auftrag')
        courseproduct = order.courseproduct
        user = self.request.user
        courseproductgroup = CourseProductGroup.objects.get(
           course=courseproduct.course)
        product_type = courseproduct.product_type

        context['order'] = order
        context['courseproduct'] = courseproduct
        context['courseproductgroup'] = courseproductgroup

        send_receipt(
            transaction = transaction,
            order=order,
            user=user,
            module=self.__module__,
        )
        return context


class PaymentFailureView(
    MessageMixin,
    TemplateView):
    """
    This view informs the customer about a payment failure
    """
    template_name = 'checkout/pages/payment_failed.html'

    def get_context_data(self, **kwargs):
        """
        gets the product and the braintree client token
        """
        context = super(PaymentFailureView, self).get_context_data(**kwargs)
        try:
            order = Order.objects.get(pk=self.kwargs['order_pk'])
        except ObjectDoesNotExist:
            logger_sentry.error('Nach der Zahlung fehlte der Auftrag')
        courseproduct = order.courseproduct
        user = self.request.user
        courseproductgroup = CourseProductGroup.objects.get(
           course=courseproduct.course)
        product_type = courseproduct.product_type

        context['order'] = order
        context['courseproduct'] = courseproduct
        context['courseproductgroup'] = courseproductgroup
        return context