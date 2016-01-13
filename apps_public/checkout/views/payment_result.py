# coding: utf-8

"""
Payment Result Views: show payment success or Payment Failure to the Customer
"""

from __future__ import unicode_literals, absolute_import

from django.views.generic import TemplateView
from django.core.exceptions import ObjectDoesNotExist

from braces.views import MessageMixin

from apps_core.email.utils.payment import send_receipt

from apps_productdata.mentoki_product.models.courseproductgroup import \
    CourseProductGroup
from apps_customerdata.customer.models.order import Order
from apps_customerdata.customer.models.transaction import Transaction

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
        context['user'] = user
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
        print "======="
        print courseproduct
        print "-----------"
        user = self.request.user
        courseproductgroup = CourseProductGroup.objects.get(
           course=courseproduct.course)
        product_type = courseproduct.product_type

        context['order'] = order
        context['courseproduct'] = courseproduct
        context['courseproductgroup'] = courseproductgroup
        return context