# coding: utf-8

"""
Braintree Integration Payment Form for Authenticated Users
"""

from __future__ import unicode_literals, absolute_import

from django import forms
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.views.generic import FormView, TemplateView
from django.core.exceptions import ObjectDoesNotExist
from django.forms import ValidationError

from django.conf import settings

import braintree

import logging
logger = logging.getLogger(__name__)

from apps_customerdata.customer.models.customer import Customer
from apps_customerdata.customer.models.transaction import \
    SuccessfulTransaction, FailedTransaction

from apps_customerdata.customer.models.order import Order
from apps_customerdata.customer.models.temporder import TempOrder

from apps_productdata.mentoki_product.models.courseproduct \
    import CourseProduct
from apps_productdata.mentoki_product.models.courseproductgroup import \
    CourseProductGroup
from apps_productdata.mentoki_product.constants import CURRENCY_CHOICES

# TODO import User from settings instead ?
from accounts.models import User


# configure the global braintree object:
braintree.Configuration.configure(
    environment=settings.BRAINTREE_ENVIRONMENT,
    merchant_id=settings.BRAINTREE['merchant_id'],
    public_key=settings.BRAINTREE['public_key'],
    private_key=settings.BRAINTREE['private_key'],
    merchant_account_id_chf=settings.BRAINTREE['merchant_account_id_chf'],
    merchant_account_id_eur=settings.BRAINTREE['merchant_account_id_eur'],
)


class PaymentForm(forms.Form):
    """
    Payment Form uses Braintrees Drop In

    The payment nounce is hidden.

    The participant data have already been stored in the temporder. It is assumed that
    the pariticipant is either logged in or new to the system.

    If someone else pays for the participant this person is just considered the participants
    method of payment.

    The customer is the participant. So in the customer table, he will be recordered
    with his userid along with his payment_customer_id for braintree.
    """
    # hidden input
    payment_method_nonce = forms.CharField()


class PaymentView(
    FormView):
    """
    This view contains the payment form.
    """
    template_name = 'checkout/pages/payment_form.html'
    form_class = PaymentForm

    def get_context_data(self, **kwargs):
        """
        gets the temporary order that already contains the participant data and
        the product and gets the braintree client token, in order to prepare
        for the payment
        """
        context = super(PaymentView, self).get_context_data(**kwargs)
        # ------------------------------------------
        # get temporary order including participant
        # ------------------------------------------

        # memorize data that is needed again during the form processing

        # temporary order
        temporder = get_object_or_404(
            TempOrder,
            pk=self.kwargs['temporder_pk'])
        context['temporder'] = temporder
        # product data
        courseproduct = temporder.courseproduct
        context['courseproduct'] = courseproduct
        context['courseproductgroup'] = get_object_or_404(CourseProductGroup,
                                               course=courseproduct.course)

        logger.debug('-------------- payment started for: %s'
             % (temporder))

        # ----------------------------------------
        # if it is an authenticated user:
        # check whether braintree customer object exist already,
        # if not prepare the data for later
        # ----------------------------------------
        braintree_token_customer_arg = {}
        if self.request.user.is_authenticated():
            try:
                customer = Customer.objects.get(user=self.request.user)
                braintree_token_customer_arg['customer_id'] = customer.braintree_customer_id
                logger.debug('user is customer: %s %s'
                             % (customer, braintree_token_customer_arg))
            except ObjectDoesNotExist:
                # that is fine too
                pass
        # ----------------------------------------
        # get client token:
        # if the customer exists at braintree his payment-methods may be
        # prefetched if his customer_id is included when requesting the token
        # --------------------------------------
        context['client_token'] = braintree.ClientToken.generate(braintree_token_customer_arg)
        logger.debug('payment token generated')

        return context

    def form_valid(self, form):
        """
        handles the transaction
        """
        # payment nounce
        nonce = form.cleaned_data['payment_method_nonce']
        logger.debug('payment nonce exists %s' % nonce)

        # ----------------------------------------
        # get temporary order and prepare date
        # ----------------------------------------
        print nonce

        temporder = get_object_or_404(
            TempOrder,
            pk=self.kwargs['temporder_pk'])

        # sales data
        amount = str(temporder.courseproduct.sales_price)
        currency = temporder.courseproduct.currency
        courseproduct = temporder.courseproduct

        # participant data
        user = self.request.user
        if not user.is_authenticated():
            first_name = temporder.participant_first_name
            last_name = temporder.participant_last_name
            email = temporder.participant_email
            username = temporder.participant_username
        else:
            first_name = user.first_name
            last_name = user.last_name
            email = user.email
            username = user.username            

        logger.debug('payment method nonce received, ready to prepare transaction')
        
        # ----------------------------------------
        # merchant account depends on the currency
        # check whether braintree customer object exist already
        # ----------------------------------------
        if currency == CURRENCY_CHOICES.chf:
            merchant_account_id = settings.BRAINTREE['merchant_account_id_chf']
        else:
            merchant_account_id = settings.BRAINTREE['merchant_account_id_eur']

        # ----------------------------------------
        # the transaction is attempted
        # it will contain customer data if the customer does not exist yet
        # ----------------------------------------
        transaction_data = {}
        transaction_data['merchant_account_id'] = merchant_account_id
        transaction_data['merchant_account_id'] = merchant_account_id
        transaction_data['payment_method_nonce'] = nonce
        transaction_data['amount'] = '14.00'
        transaction_data['options'] = {
                    'submit_for_settlement': True,
                    'store_in_vault_on_success': True,
                }
        if not hasattr(user, 'customer'):
            # customer data will be created along with the transaction
            transaction_data['customer'] = {
                            "first_name": first_name,
                            "last_name": last_name,
                            "email": email
                          }
        result = braintree.Transaction.sale(transaction_data)
        logger.debug('prepare transaction %s'
                     % (transaction_data))

        # ---------------------------
        # if the result is success, create user, customer and transaction object
        # and order
        # ---------------------------
        if result.is_success:
            logger.debug('the transaction was successful %s'
                         % (result.transaction.id))
            if not user.is_authenticated():
                #create a user object
                user = User.objects.create_user(
                    username = username,
                    email = email,
                    first_name = first_name,
                    last_name = last_name
                )
            logger.debug('new user created %s'
                         % (user))

            if not hasattr(user, 'customer'):
                # create a customer object
                customer = Customer.objects.create_new_customer(
                    braintree_customer_id=result.transaction.customer['id'],
                    first_name=first_name,
                    last_name=last_name,
                    user=user,
                    email=email,
                )
                logger.debug('new customer created %s: %s'
                             % (customer, result.transaction.customer['id']))
            else:
                customer = user.customer

            #create order
            order = Order.objects.create(
                courseproduct=courseproduct,
                customer=customer,
                income=amount,
                currency=currency
            )
            self.transaction = SuccessfulTransaction.objects.create(
                braintree_transaction_id=result.transaction.id,
                amount=amount,
                currency=currency,
                braintree_merchant_account_id=merchant_account_id,
                order=order,
                customer=customer
            )
        # ---------------------------
        # if the result is not success, store result in
        # failed_transaction
        # ---------------------------
        else:
            if result.errors:
                #parameters were wrong, no transaction_object will be present
                temporder.errors = result.errors
                temporder.save()

                raise ValidationError('''Bei der Bearbeitung Ihrer Zahlung ist
                    etwas schief gelaufen. Wir haben Ihren Buchungswunsch
                    aufgenommen und kontaktieren Sie innerhalb eines Tages''')

            else:
                # creditcard declined, etc.
                # inform Customer
                FailedTransaction.objects.create(
                    braintree_transaction_id=result.transaction.id,
                    amount=amount,
                    currency=currency,
                    braintree_merchant_account_id=merchant_account_id,
                    temporder=temporder
                )
                raise ValidationError('''Ihre Kreditkarte wurde abgelehnt oder
                etwas ähnliches.''')

        # redirect to thank you page.
        return super(PaymentView, self).form_valid(form)


    def get_success_url(self):
        """
        redirects to the success page after paying
        """
        return reverse('checkout:payment_success',
                       kwargs={'slug': self.kwargs['slug'],
                               'pk': self.transaction.pk})