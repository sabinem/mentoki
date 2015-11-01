# coding: utf-8

"""
Braintree Integration Payment View
handles payment for authenticated users

Users are expected to be authenticated and have their
email verified in order to be able to pay.

If the are unregistered and try to book they are guided
through this process until they are registered, they email
was confirmed and they have been guided back to their initial
booking intention
"""

from __future__ import unicode_literals, absolute_import

from django import forms
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.views.generic import FormView
from django.core.exceptions import ObjectDoesNotExist
from django.forms import ValidationError
from django.utils.decorators import method_decorator
from django.db import IntegrityError
from django.http import HttpResponseRedirect

from django.conf import settings

from braces.views import MessageMixin, UserPassesTestMixin

import braintree
from braintree.exceptions import AuthenticationError, AuthorizationError, \
    DownForMaintenanceError, ServerError, UnexpectedError, NotFoundError


from allauth.account.decorators import verified_email_required

from apps_customerdata.customer.models.customer import Customer
from apps_customerdata.customer.models.transaction import Transaction
from apps_customerdata.customer.models.order import Order
from apps_customerdata.customer.constants import TRANSACTION_ERROR_CODE

from apps_productdata.mentoki_product.models.courseproductgroup import \
    CourseProductGroup
from apps_productdata.mentoki_product.models.courseproduct import CourseProduct
from apps_productdata.mentoki_product.constants import CURRENCY_CHOICES
from apps_customerdata.customer.constants import ORDER_STATUS, \
    ORDER_STATUS_UNPAID
from apps_data.courseevent.models.courseevent import CourseEventParticipation

import logging
logger = logging.getLogger(__name__)


# configure the global braintree object:
braintree.Configuration.configure(
    environment=settings.BRAINTREE_ENVIRONMENT,
    merchant_id=settings.BRAINTREE['merchant_id'],
    public_key=settings.BRAINTREE['public_key'],
    private_key=settings.BRAINTREE['private_key'],
    merchant_account_id_chf=settings.BRAINTREE['merchant_account_id_chf'],
    merchant_account_id_eur=settings.BRAINTREE['merchant_account_id_eur'],
)


class AuthMixin(UserPassesTestMixin):
    """
    this Mixin builds the menu in the side-bar and the top of the page.
    """
    raise_exception = False
    login_url = settings.LOGIN_REDIRECT_URL
    redirect_field_name = settings.LOGIN_REDIRECT_URL

    def test_func(self, user):

        """
        This function belongs to the Braces Mixin UserPasesTest: test for using the course backend.
        Only the Superuser and the owner of the course are allowed
        """
        course = get_object_or_404(Course, slug=self.kwargs['course_slug'])

        if user.is_superuser:
            self.request.session['workon_course_id'] = course.id
            return True

        else:

            if course.is_owner(user):
                self.request.session['workon_course_id'] = course.id
                return True

        self.messages.warning(_('You are not allowed to change this data since you are not a teacher of this course.'))

        return None


class PaymentForm(forms.Form):
    """
    Payment Form uses Braintrees Drop In

    The payment nounce is hidden.

    If someone else pays for the participant this person is just considered
    the participants method of payment. So the customer is always the
    participant himself.

    Since only logged in users can book, everything beside the nonce is
    already set when entering this form
    """
    payment_method_nonce = forms.CharField() # hidden input


class PaymentView(
    UserPassesTestMixin,
    MessageMixin,
    FormView):
    """
    This view handles the payment process for courseproducts.

    :prerequistes: the user is assumed to be logged in and have his email
    confirmed before he can pay.
    :param slug that is the CourseProduct.slug
    :return: redirects to a "success" page, where the user is told about what
    happened
    """
    template_name = 'checkout/pages/payment_form.html'
    form_class = PaymentForm
    amount = None
    redirect_field_name = settings.COURSE_LIST_URL

    def test_func(self, user):
        """
        tests whether the logged in user may book this product
        """
        courseproduct = get_object_or_404(
            CourseProduct,
            slug=self.kwargs['slug'])
        if hasattr(user, 'customer'):
            customer=user.customer
            logger.debug('1. user is a customer [%s]' % customer)
            ordered_products = \
                Order.objects.\
                products_with_order_paid_for_course_and_customer(
                    course=courseproduct.course,
                    customer=user.customer)
            if courseproduct.available_with_past_orders(ordered_products):
                return True
            self.messages.warning('''Du kannst dieses Produkt nicht buchen,
                weil es sich mit Kursen überschneidet,
                die Du bereits gebucht hast.''')
            return None
        else:
            return True

    @method_decorator(verified_email_required)
    def dispatch(self, request, *args, **kwargs):
        """
        The users email needs to be verified before booking a course.
        This makes use of allauth decorator @verified_email_required.
        """
        logger.debug('dispatch payment view')
        return super(PaymentView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        """
        gets the product data and the payment nounce,

        the method to create the token at braintree gets the following
        arguments:
        - braintree id of the customer
        - braintree_merchant_id according to the currency of the payment
        """
        logger.debug('===========get context data for payment')
        context = super(PaymentView, self).get_context_data(**kwargs)
        # ------------------------------------------
        # get productdata or 404: this really is a 404, if the product
        # is not found
        # ------------------------------------------
        courseproduct = get_object_or_404(
            CourseProduct,
            slug=self.kwargs['slug'])
        courseproductgroup = get_object_or_404(
            CourseProductGroup,
            course=courseproduct.course)
        logger.info(
            'product data found: group[%s]product[%s]amount[%s]currency[%s]'
                 % (courseproductgroup,
                    courseproduct.sales_price,
                    courseproduct,
                    courseproduct.currency))
        # ------------------------------------------
        # reset args for generating the client token
        # ------------------------------------------
        braintree_token_args = {}
        # ------------------------------------------
        # set merchant id according to product currency
        # ------------------------------------------
        if courseproduct.currency == CURRENCY_CHOICES.chf:
            braintree_token_args['merchant_account_id'] = \
                settings.BRAINTREE['merchant_account_id_chf']
        elif courseproduct.currency == CURRENCY_CHOICES.euro:
            braintree_token_args['merchant_account_id'] = \
                settings.BRAINTREE['merchant_account_id_eur']
        else:
            logger.error(
                'Unknown currency for courseproduct [%s]' % (courseproduct))
        # ------------------------------------------
        # get braintree customer id, if it exists
        # ------------------------------------------
        user=self.request.user
        try:
            customer = Customer.objects.get(user=user)
            braintree_token_args['customer_id'] \
                = customer.braintree_customer_id
            logger.debug('customer [%s] found with braintree customer_id[%s]'
                         % (customer, customer.braintree_customer_id))
        except ObjectDoesNotExist:
            # new customer, does not have braintree entry yet
            logger.info('no customer data was found')
        # ----------------------------------------
        # get client token from braintree
        # --------------------------------------
        token=None
        try:
            logger.debug('generating token with args [%s]'
                         % braintree_token_args)
            token = braintree.ClientToken.generate(
                braintree_token_args)
            logger.info('payment token sucessfully generated')
        except Exception as ex:
            template = "An exception of type {0} occured. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            logger.error(message)
        # ------------------------------------------
        # set context
        # ------------------------------------------
        context['courseproductgroup'] = courseproductgroup
        context['courseproduct'] = courseproduct
        context['client_token'] = token
        return context


    def form_valid(self, form):
        """
        Since the customer tried to pay it is assumed this is serious.
        So all the objects necessary for proessing the payments are
        established to document the attempt: this is:
        1. the customer: get or create
        2. the order: get or create
        3. the transaction: create
        These objects are there before the actual transaction with braintree
        happens. They are all updated according to the result of the braintree
        interaction and the user is send to a success or error page.
        :param form with nonce
        :return: updated customer, order and transaction
        """
        # ------------------------------------------
        # get nonce
        # ------------------------------------------
        logger.debug('===========in form valid')
        nonce = form.cleaned_data['payment_method_nonce']
        self.payment_success = False # memorize payemnt success or failure
        # ------------------------------------------
        # product data has to be fetched again
        # ------------------------------------------
        courseproduct_slug = self.kwargs['slug']
        courseproduct = get_object_or_404(
            CourseProduct,
            slug=self.kwargs['slug'])
        user = self.request.user
        amount = courseproduct.sales_price
        currency = courseproduct.currency
        logger.debug('''starting transaction for product [%s]
                     user [%s] amount [%s] currency [%s]'''
                     % (courseproduct,
                        user,
                        amount,
                        currency))
        # ----------------------------------------
        # create or get customer object
        # ----------------------------------------
        customer, created = Customer.objects.get_or_create(
            user=user)
        logger.debug('customer [%s] created: [%s] braintree_id: [%s]'
                     % (customer,
                        created,
                        customer.braintree_customer_id))
        # ----------------------------------------
        # create or get order object
        # ----------------------------------------
        self.order, created = Order.objects.get_or_create(
            courseproduct=courseproduct,
            customer=customer,
            defaults={
                'amount':amount,
                'currency':currency,
                'email':user.email,
                'first_name':user.first_name,
                'last_name':user.last_name}
        )
        logger.debug('order [%s] created: [%s]'
                     % (self.order,
                        created))
        # ----------------------------------------
        # prepare transaction object
        # ----------------------------------------
        self.transaction = Transaction.objects.create(
            amount=amount,
            currency=currency,
            customer=customer,
            order=self.order,
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name,
            course=courseproduct.course
        )
        logger.debug('transaction created: [%s]'
                     % (self.transaction))
        if not self.order.order_status in ORDER_STATUS_UNPAID:
            logger.debug('order [%s] is already paid, status: [%s] '
                         % (self.order,
                            self.order.order_status))
            self.transaction.flag_payment_sucess = False
            self.transaction.error_code = TRANSACTION_ERROR_CODE.already_paid
            self.transaction.save()
            return super(PaymentView, self).form_valid(form)
        # ----------------------------------------
        # the transaction is attempted
        # it will contain customer data if the customer does not exist yet
        # ----------------------------------------
        transaction_data = {}
        transaction_data['payment_method_nonce'] = nonce
        transaction_data['amount'] = str(amount)
        transaction_data['options'] = {
                    'submit_for_settlement': True,
                    'store_in_vault_on_success': True,
                }
        transaction_data['order_id'] = self.order.id
        #transaction_data['descriptor'] = order.courseproduct.descriptor

        # customer data will be created along with the transaction
        if not customer.braintree_customer_id:
            transaction_data['customer'] = {
                            "first_name": user.first_name,
                            "last_name": user.last_name,
                            "email": user.email
                          }
        logger.debug('prepare transaction %s'
                     % (transaction_data))
        result = braintree.Transaction.sale(transaction_data)
        logger.debug('result [%s]'
                     % (transaction_data))
        # ----------------------------------------
        # react on transaction result
        # ----------------------------------------
        if result.is_success:
            self.transaction.amount = result.transaction.amount
            self.transaction.flag_payment_sucess=True
            self.transaction.braintree_customer_id = \
                result.transaction.customer['id']
            self.transaction.braintree_merchant_account_id \
                = result.transaction.merchant_account_id
            self.transaction.braintree_transaction_id = result.transaction.id
            self.transaction.braintree_payment_token = \
                result.transaction.credit_card['token']
            self.transaction.save()
            if not customer.braintree_customer_id:
                customer.braintree_customer_id = \
                    result.transaction.customer['id']
                customer.save()
            self.order.order_status = ORDER_STATUS.paid
            self.order.save()
            self.payment_success = True
        # ----------------------------------------
        # register for courseevent on success
        # ----------------------------------------
            if courseproduct.product_type.is_courseevent_participation:
                # set up courseevent participation
                participation, created =\
                CourseEventParticipation.objects.get_or_create(
                    user=user,
                    courseevent=courseproduct.courseevent)
                if participation:
                    logger.debug('participation: [%s] created:[%s]'
                                 % (participation, created))

        # ----------------------------------------
        # react on errors
        # ----------------------------------------
        else:
            self.transaction.flag_payment_sucess=False
            if self.transaction:
                logger.debug('transaction there [%s] but no success'
                     % (self.transaction))
                pass
            else:
                message = ""
                for error in result.errors.deep_errors:
                    message += ("CODE: %s MESSAGE: %s \n" %
                    (error.code, error.message))
                self.transaction.braintree_error_details = message
                self.transaction.save()
                logger.debug('error during transaction [%s]'
                     % (self.transaction.errors))
        return super(PaymentView, self).form_valid(form)

    def get_success_url(self):
        """
        redirects in case of payment success or failure
        :return: url
        """
        if self.payment_success:

            return reverse('checkout:payment_success',
                          kwargs={'order_pk': self.order.pk,
                                  'slug': self.kwargs['slug']})
        else:
            return reverse('checkout:payment_failure',
                          kwargs={'transaction_pk': self.transaction.pk,
                                  'slug': self.kwargs['slug']})

