# coding: utf-8

"""
Braintree Integration Payment Form
"""

from __future__ import unicode_literals, absolute_import

from django.conf import settings
from django import forms
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.views.generic import FormView, TemplateView
from django.core.exceptions import ObjectDoesNotExist

import braintree

import logging
logger = logging.getLogger(__name__)

from apps_customerdata.customer.models import Customer
from apps_customerdata.transaction.models.transaction import Transaction
from apps_customerdata.mentoki_product.models.courseevent \
    import CourseEventProduct

from .info import CourseEventProductMixin


# configure the global braintree object:
braintree.Configuration.configure(
    environment=settings.BRAINTREE_ENVIRONMENT,
    merchant_id=settings.BRAINTREE['merchant_id'],
    public_key=settings.BRAINTREE['public_key'],
    private_key=settings.BRAINTREE['private_key'],
    merchant_account_id_chf=settings.BRAINTREE['merchant_account_id_chf'],
    merchant_account_id_eur=settings.BRAINTREE['merchant_account_id_eur'],
)

class BraintreeForm(forms.Form):
    """
    Payment Form uses Braintrees Drop In
    """
    payment_method_nonce = forms.CharField()
    agbs_read = forms.CharField(widget=forms.CheckboxInput)


class PaymentView(
    FormView):
    """
    This view contains the payment form.
    """
    template_name = 'courseoffer/pages/payment_form.html'
    form_class = BraintreeForm

    def get_context_data(self, **kwargs):
        """
        gets the product and the braintree client token
        """
        context = super(PaymentView, self).get_context_data(**kwargs)
        context['url_name'] = self.request.resolver_match.url_name

        courseeventproduct = get_object_or_404(CourseEventProduct,pk=self.kwargs['pk'])
        context['courseeventproduct'] = courseeventproduct
        logger.debug('payment started for: %s %s'
                     % (self.request.user, courseeventproduct))

        context['client_token'] = braintree.ClientToken.generate()
        logger.debug('payment toke generated: %s'
                     % context['client_token'])

        return context

    def get_success_url(self):
        """
        redirects to the success page after paying
        """
        return reverse('courseoffer:payment_success', kwargs={'slug': self.kwargs['slug']})

    def form_valid(self, form):
        """
        handles the transaction and the customer identification
        """

        nonce = form.cleaned_data['payment_method_nonce']

        logger.debug('payment method nonce received: %s'
                     % nonce)

        user = self.request.user

        # create a customer
        # https://developers.braintreepayments.com/javascript+python/reference/response/customer
        try:

            customer = Customer.objects.get(user=user)
            logger.debug('user is customer: %s %s'
                         % (customer, customer.braintree_customer_id))

        except ObjectDoesNotExist:

            result = braintree.Customer.create({
              'first_name': user.first_name,
              'last_name': user.last_name
            })

            logger.debug('result braintree customer creation: %s'
                         % (result))

            if result.is_success:
                # create a customer object
                customer = Customer.objects.create(
                    braintree_customer_id=result.customer.id,
                    user=user
                )
                logger.debug('create new mentoki customer: %s %s'
                             % (customer, customer.braintree_customer_id))
            else:
                raise Exception('Kunde konnte nicht angelegt werden. %s' % result)

        # Prepare the transaction
        # https://developers.braintreepayments.com/javascript+python/reference/request/transaction/sale

        product = get_object_or_404(CourseEventProduct, pk=self.kwargs['pk'])

        amount = str(product.price_total())

        braintree_merchant_account_id = settings.BRAINTREE['merchant_account_id_chf']

        transaction_data = {
            'amount': amount,
            'options': {
                'submit_for_settlement': True,
                'store_in_vault_on_success': True,
            },
            #'descriptor': {
            #    'name': 'Mentoki',
            #},
            'merchant_account_id': braintree_merchant_account_id,
            'payment_method_nonce': nonce,
        }
        logger.debug('prepare transaction %s'
                     % (transaction_data))

        result = braintree.Transaction.sale(transaction_data)

        logger.debug('react to transaction result %s'
                     % (result))

        # TODO: Check if the payment went through

        if not result.is_success:
            logger.warning('Payment Error: %s' % result.message)
            return self.form_invalid(form)

        transaction = Transaction.objects.create(
            braintree_customer_id=customer.braintree_customer_id,
            braintree_transaction_id=result.transaction.id,
            amount=amount,
            currency=product.currency,
            braintree_merchant_account_id=braintree_merchant_account_id,
            product=product,
            customer=customer
        )
        logger.debug('transaction saved %s'
                     % (transaction))

        # redirect to thank you page.
        return super(PaymentView, self).form_valid(form)


class SuccessView(
    CourseEventProductMixin,
    TemplateView):
    """
    This view is called if the payment has been successful.
    """
    template_name = 'courseoffer/pages/payment_sucessful.html'