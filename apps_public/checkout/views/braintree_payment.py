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
from apps_customerdata.customer.models.transaction import Transaction
from apps_customerdata.customer.models.order import Order
from apps_customerdata.customer.models.temporder import TempOrder

from apps_productdata.mentoki_product.models.courseproduct \
    import CourseProduct
from apps_productdata.mentoki_product.models.courseproductgroup import \
    CourseProductGroup

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


class PaymentForm(forms.ModelForm):
    """
    Payment Form uses Braintrees Drop In

    The payment nounce is hidden.

    The participant data have already been stored in the temporder. It is assumed that
    the pariticipant is either logged in or new to the system.

    Therefore the payer, if different from the participant may be a known in the system, but can't
    be aaked to login as well.

    It must be checked whether a braintree customer exists for that email. Since the email
    serves as identification this should be good enough.

    """
    # hidden input
    payment_method_nonce = forms.CharField()
    logged_in_user_paying = forms.BooleanField()

    class Meta:
        model = Customer
        fields = ('email', 'first_name',
                  'last_name')

    def __init__(self, *args, **kwargs):
        """
        The init gets the product and the user
        """
        # get product
        courseproduct_slug = kwargs.pop('courseproduct_slug', None)
        self.courseproduct = get_object_or_404(CourseProduct, slug=courseproduct_slug)
        # get user if logged in
        self.user = kwargs.pop('user', None)
        super(PaymentForm, self).__init__(*args, **kwargs)

    def clean(self):
        """
        If the email already exists the user is asked to log in first.
        """
        # check whether user exists already

        try:
            # a user that is logged in pays himself: he is the customer
            if self.user.is_authenticated and self.cleaned_data['logged_in_user_paying']:
                customer = Customer.objects.get(user=self.user)
            else:
                # someone else is paying
                customer = Customer.objects.get(email=self.cleaned_data['email'])
        except ObjectDoesNotExist:
            # create braintree customer
            result = braintree.Customer.create({
              'first_name': self.cleaned_data['first_name'],
              'last_name': self.cleaned_data['last_name'],
              'email': self.cleaned_data['email']
            })

            customer_exists = False
        else :
            try:
                # someone else is paying
                customer = Customer.objects.get(email=self.cleaned_data['email'])
            except ObjectDoesNotExist:
                #
                customer_exists = False



        Customer.objects.get(user=user)

        email = email = self.cleaned_data['email']
        try:
            User.objects.get(email=email)
            raise ValidationError('Du bist schon bei Mentoki registriert. '
                                  'Bitte melde Dich an, bevor Du den Kurs bezahlst.')
        except ObjectDoesNotExist:
            pass

        # check whether user ordered this product already
        try:
            Order.objects.get(courseproduct=self.courseproduct,
                              participant_email=self.cleaned_data['email'])
            raise ValidationError('Du hast diesen Kurs schon für diesen Teilnehmer gekauft')
        except ObjectDoesNotExist:
            pass
        return self.cleaned_data


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

        temporder = get_object_or_404(
            TempOrder,
            pk=self.kwargs['temporder_pk'])
        courseproduct = temporder.courseproduct
        courseproductgroup = get_object_or_404(CourseProductGroup,
                                               course=courseproduct.course)
        context['courseproductgroup'] = courseproductgroup
        context['courseproduct'] = courseproduct
        context['user'] = self.request.user
        context['temporder'] = temporder

        logger.debug('-------------- payment started for: %s %s'
                     % (self.request.user, courseproduct))

        #TODO: if user is authenticated. Check if he already bought the product

        context['client_token'] = braintree.ClientToken.generate()
        logger.debug('payment token generated')

        return context

    def get_form_kwargs(self):
        """
        save the user and the product data for the form, to check
        wether there is already an order for that combination.
        """
        if self.request.user.is_authenticated():
            user = self.request.user
        courseproduct_slug = self.kwargs['slug']
        kwargs = super(PaymentView, self).get_form_kwargs()
        if self.request.user.is_authenticated():
            kwargs['user']= user
        kwargs['courseproduct_slug'] = courseproduct_slug
        return kwargs

    def form_valid(self, form):
        """
        handles the transaction and the customer identification
        """
        nonce = form.cleaned_data['payment_method_nonce']
        logger.debug('payment method nonce received')

        user = self.request.user
        braintree_customer_exists = False

        if user.is_authenticated():

            # steps for authenticated user:
            # 1. braintree customer object exist

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
        # 4. Particpant is registerd as a user

        # redirect to thank you page.
        return super(PaymentView, self).form_valid(form)


    def get_success_url(self):
        """
        redirects to the success page after paying
        """
        return reverse('courseoffer:payment_success',
                       kwargs={'slug': self.kwargs['slug'],
                               'pk': self.object.pk})