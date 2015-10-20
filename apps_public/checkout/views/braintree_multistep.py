# coding: utf-8

"""
Braintree Integration Payment Form
"""

from __future__ import unicode_literals, absolute_import

import floppyforms.__future__ as forms

from django.conf import settings

from django import forms
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.views.generic import FormView, TemplateView
from django.core.exceptions import ObjectDoesNotExist
from django.forms import ValidationError

from formtools.wizard.views import SessionWizardView

from django.conf import settings

import braintree

import logging
logger = logging.getLogger(__name__)

from apps_customerdata.customer.models.customer import Customer
from apps_customerdata.customer.models.transaction import Transaction
from apps_productdata.mentoki_product.models.courseproduct \
    import CourseProduct

from apps_public.storefront.views.info import CourseGroupMixin
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


class NewCustomerForm1(forms.ModelForm):
    """
    Payment Form uses Braintrees Drop In
    """
    payment_method_nonce = forms.CharField()
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(NewCustomerForm1, self).__init__(*args, **kwargs)

    def clean(self):
        if not self.user.is_authenticated():
            try:
                # TODO get User form settings?
                # TODO compare emails so that capitalsation does not matter
                User.objects.get(email=self.cleaned_data['email'])
                raise ValidationError('''Ihre Email existiert schon im System.
                                      Loggen Sie sich bitte ein.''')
            except ObjectDoesNotExist:
                pass
        return self.cleaned_data


class RecurringCustomerForm1(forms.Form):
    """
    Payment Form uses Braintrees Drop In
    """
    payment_method_nonce = forms.CharField()



class PaymentView(
    FormView):
    """
    This view contains the payment form.
    """
    template_name = 'checkout/pages/payment_form.html'

    def get_context_data(self, **kwargs):
        """
        gets the product and the braintree client token
        """
        context = super(PaymentView, self).get_context_data(**kwargs)
        context['url_name'] = self.request.resolver_match.url_name

        courseeventproduct = get_object_or_404(CourseProduct,slug=self.kwargs['slug'])
        context['courseeventproduct'] = courseeventproduct
        logger.debug('-------------- payment started for: %s %s'
                     % (self.request.user, courseeventproduct))

        #TODO: if user is authenticated. Check if he already bought the product

        context['client_token'] = braintree.ClientToken.generate()
        logger.debug('payment token generated')
        return context

    def get_form_class(self):
        if self.request.user.is_authenticated():
            return RecurringCustomerForm
        else:
            return NewCustomerForm

    def get_form_kwargs(self):

        if not self.request.user.is_authenticated():
            user = self.request.user
        kwargs = super(PaymentView, self).get_form_kwargs()
        if not self.request.user.is_authenticated():
            kwargs['user']=user
        return kwargs


    def get_success_url(self):
        """
        redirects to the success page after paying
        """
        return reverse('courseoffer:payment_success',
                       kwargs={'slug': self.kwargs['slug'],
                               'pk': self.object.pk})

    def form_valid(self, form):
        """
        handles the transaction and the customer identification
        """
        nonce = form.cleaned_data['payment_method_nonce']
        logger.debug('payment method nonce received')

        user = self.request.user
        braintree_customer_exists = False

        if user.is_authenticated():

            # create a customer
            # https://developers.braintreepayments.com/javascript+python/reference/response/customer
            try:

                customer = Customer.objects.get(user=user)

                braintree_customer_exists = True
                logger.debug('user is customer: %s %s'
                             % (customer, customer.braintree_customer_id))

            except ObjectDoesNotExist:
                pass

        if not braintree_customer_exists:

            # create braintree customer
            if user.is_authenticated():
                first_name = user.first_name
                last_name = user.last_name
                email = user.email
                user = user
                authenticated_user = True
            else:
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                email = form.cleaned_data['email']
                authenticated_user = False
            print ("userdata %s %s %s") % (first_name, last_name, email)

            # create braintree customer
            result = braintree.Customer.create({
              'first_name': first_name,
              'last_name': last_name,
              'email': email
            })

            logger.debug('result braintree customer creation: %s'
                         % (result))

            if result.is_success:

                if not user.is_authenticated():
                    #create a user object
                    user = User.objects.create_user(
                        username = form.cleaned_data['username'],
                        email = form.cleaned_data['email'],
                        first_name = form.cleaned_data['first_name'],
                        last_name =form.cleaned_data['last_name']
                    )

                # create a customer object
                customer = Customer.objects.create(
                    braintree_customer_id=result.customer.id,
                    first_name=first_name,
                    last_name=last_name,
                    user=user,
                    email=email,
                    authenticated_user=authenticated_user
                )

                logger.debug('create new mentoki customer: %s %s'
                             % (customer, customer.braintree_customer_id))
            else:
                #TODO: better inform client that he should contact me. Also error in log -> Sentry
                # I do not want the system to crash, but still get notice per email
                raise Exception('Kunde konnte nicht angelegt werden. %s' % result)

        # Prepare the transaction
        # https://developers.braintreepayments.com/javascript+python/reference/request/transaction/sale

        product = get_object_or_404(CourseProduct, slug=self.kwargs['slug'])

        amount = product.price

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

        self.object = Transaction.objects.create(
            braintree_transaction_id=result.transaction.id,
            amount=amount,
            currency=product.currency,
            braintree_merchant_account_id=braintree_merchant_account_id,
            product=product,
            customer=customer
        )
        logger.debug('transaction saved %s'
                     % (self.object))

        #TODO: register participant for courseevent

        # redirect to thank you page.
        return super(PaymentView, self).form_valid(form)


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