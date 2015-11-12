# coding: utf-8

"""
Braintree Integration Payment View
handles payment for authenticated users

Users are expected to be authenticated and have their
email verified in order to be able to pay.
"""

from __future__ import unicode_literals, absolute_import

from django import forms
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.views.generic import FormView
from django.core.exceptions import ObjectDoesNotExist
from django.forms import ValidationError
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.db import IntegrityError
from django.views.decorators.cache import cache_control

from django.conf import settings

from braces.views import MessageMixin, UserPassesTestMixin, FormMessagesMixin

import braintree
from braintree.exceptions import AuthenticationError, AuthorizationError, \
    DownForMaintenanceError, ServerError, UnexpectedError, NotFoundError
from braintree.exceptions.braintree_error import BraintreeError

from allauth.account.decorators import verified_email_required

from apps_customerdata.customer.models.customer import Customer
from apps_customerdata.customer.models.transaction import Transaction
from apps_customerdata.customer.models.order import Order
from apps_customerdata.customer.constants import TransactionErrorCode

from apps_productdata.mentoki_product.models.courseproductgroup import \
    CourseProductGroup
from apps_productdata.mentoki_product.models.courseproduct import CourseProduct
from apps_productdata.mentoki_product.constants import Currency
from apps_customerdata.customer.constants import OrderStatus
from apps_data.courseevent.models.courseevent import CourseEventParticipation
from apps_productdata.mentoki_product.constants import ProductToCustomer

from ..constants import PaymentErrorCode

import logging
logger = logging.getLogger('payments')
logger_sentry = logging.getLogger('sentry')


# configure the global braintree object:
braintree.Configuration.configure(
    environment=settings.BRAINTREE_ENVIRONMENT,
    merchant_id=settings.BRAINTREE['merchant_id'],
    public_key='xxx',
    private_key=settings.BRAINTREE['private_key'],
    merchant_account_id_chf=settings.BRAINTREE['merchant_account_id_chf'],
    merchant_account_id_eur=settings.BRAINTREE['merchant_account_id_eur'],
)

class AuthMixin(UserPassesTestMixin):

    redirect_field_name = settings.COURSE_LIST_URL

    def test_func(self, user):
        """
        tests whether the logged in user may book this product
        """
        courseproduct = get_object_or_404(
            CourseProduct,
            slug=self.kwargs['slug'])
        logger.info('Teste, ob Benutzer [%s] das Produkt [%s] kaufen kann.'
                     % (user, courseproduct))
        if hasattr(user, 'customer'):
            customer=user.customer
            ordered_products = \
                Order.objects.\
                products_with_order_paid_for_course_and_customer(
                    course=courseproduct.course,
                    customer=user.customer)
            if (courseproduct.available_with_past_orders(ordered_products)
                == ProductToCustomer.AVAILABLE):
                logger.info('ja, kann er, denn es verträgt'
                    ' sich mit seinen bisher gekauften Produkten')
                return True
            self.messages.warning('Du kannst dieses Produkt nicht buchen, '
                'weil es sich mit Kursen überschneidet, '
                'die Du bereits gebucht hast.')
            logger.info('nein, kann er nicht: denn es verträgt sich nicht '
                'mit den bereits bestellten Produkten.')
            return None
        else:
            logger.info('nein, kann er, denn er ist noch kein Kunde')
            return True


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
    MessageMixin,
    AuthMixin,
    FormView):
    """
    This view handles the payment process for courseproducts.

    :prerequistes: the user is assumed to be logged in and have his email
    confirmed before he can pay.
    :param slug that is the CourseProduct.slug
    :return: redirects to a "success" page, where the user is told about what
    happened
    """
    form_invalid_message = "Something went wrong, post was not saved"
    template_name = 'checkout/pages/payment_form.html'
    form_class = PaymentForm
    amount = None

    @cache_control(no_cache=True, must_revalidate=True)
    @method_decorator(verified_email_required)
    def dispatch(self, request, *args, **kwargs):
        """
        The users email needs to be verified before booking a course.
        This makes use of allauth decorator @verified_email_required.
        """
        logger.info('-------------- neuer Zahlungsaufruf')
        return super(PaymentView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.get_form()
        context = self.get_context_data(form=form)
        self.x = "merken"
        self.request.session['x'] = "y"
        if 1 == 2:
            return self.redirect_on_error()
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        return Super(PaymentView, self).get_context_data(request, *args, **kwargs)
        if 'view' not in kwargs:
            kwargs['view'] = self
        #if 1 == 1:
            #return self.redirect_on_error()
        return kwargs

    def redirect_on_error(self):
        """
        redirects on error
        :param kwargs: transaction_id and slug of the courseproductgroup
        :return: response that redirects to the error page
        """
        return HttpResponseRedirect(reverse(
            'checkout:payment_failure',
            kwargs={'transaction_pk':107,
                    'slug':self.kwargs['slug']}))


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
        y=x
        try:
            transaction_id = self.request.session['transaction_id']
            Transaction.objects.get(pk=transaction_id)
        except ObjectDoesNotExist:

            return self.redirect_on_error(**kwargs)

        nonce = form.cleaned_data['payment_method_nonce']
        logger.info('Das Token gefunden.')
        # ------------------------------------------
        # get the order
        # ------------------------------------------
        transaction = transaction.objects.get()
        user = self.request.user
        amount = courseproduct.sales_price
        currency = courseproduct.get_currency_display
        logger.info('Die Transaction wird vorbereitet für Benutzer:[%s],'
                     ' Produkt:[%s], Betrag:[%s] in der Währung:[%s]'
                     % (courseproduct,
                        user,
                        amount,
                        currency))
        # ----------------------------------------
        # create or get customer object
        # ----------------------------------------
        customer, created = Customer.objects.get_or_create(
            user=user)
        if created:
            logger.info('Der Kunde [%s] wurde bei mentoki neu angelegt mit der '
                         'braintree id [%s]'
                         % (customer,
                            customer.braintree_customer_id))
        else:
            logger.info('Der Kunde [%s] mit der '
                         'braintree id [%s] wurde bei mentoki gefunden'
                         % (customer,
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
        if created:
            logger.info('Ein Auftrag [%s] wurde bei neu mentoki angelegt.'
                         % (self.order))
        else:
            logger.info('Es gab schon einen Auftrag [%s] im Status [%s] zu '
                         'dieser Buchung, er wurde fürs Update vorbereitet.'
                         % (self.order, self.order.order_status))
            if self.order.order_status == OrderStatus.PAID:
                logger.error('Die Bestellung [%s] ist bereits bezahlt: '
                             'Status:[%s]'
                             % (self.order,
                                self.order.order_status))
                return super(PaymentView, self).form_valid(form)
                    #do not pay double!
        # ----------------------------------------
        # prepare transaction object
        # ----------------------------------------
        self.transaction = Transaction.objects.create(
            amount=amount,
            currency=currency,
            customer=customer,
            order=order,
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name,
            course=courseproduct.course
        )
        logger.info('Eine Transaktion [%s] wurde bei Mentoki angelegt und'
                     ' fürs Update vorbereitet.'
                     % (self.transaction))
        # ----------------------------------------
        # the transaction is attempted
        # it will contain customer data if the customer does not exist yet
        # ----------------------------------------
        transaction_data = {}
        transaction_data['amount'] = str(amount)
        transaction_data['options'] = {
                    'submit_for_settlement': True,
                    'store_in_vault_on_success': True,
                }
        transaction_data['order_id'] = self.order.id
        # customer data will be created along with the transaction
        if not customer.braintree_customer_id:
            transaction_data['customer'] = {
                            "first_name": user.first_name,
                            "last_name": user.last_name,
                            "email": user.email
                          }
        logger.info('Braintree Transaktion mit folgendem Input (Token wird '
                    'nicht angezeigt): [%s]'
                     % (transaction_data))
        transaction_data['payment_method_nonce'] = nonce
        result = braintree.Transaction.sale(transaction_data)
        event_logger.info('Braintree Transaktion mit folgendem Input (Token wird '
                    'nicht angezeigt): [%s] hatte Erfolg [%s]. Braintree '
                    'Transaktionsnr. [%s], Mentoki Transaktion [%s] '
                     % (transaction_data, result.is_success,
                        result.transaction.id, self.transaction))

        # ----------------------------------------
        # react on transaction result
        # ----------------------------------------
        if result.is_success:
            logger.info('Die Transaktion hatte Erfolg. Diese Transaction'
                        ' kam von braintree zurück: [%s]' %
                        braintree.transaction)
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
            logger.info('Die Transaktion wurde bei mentoki gespeichert: [%s]'
                        % self.transaction)
            if not customer.braintree_customer_id:
                customer.braintree_customer_id = \
                    result.transaction.customer['id']
                customer.save()
                logger.info('Der Kunde wurde bei mentoki upgedated: '
                            '[%s] mit der braintree id [%s]'
                            % (customer, customer.braintree_customer_id))

            self.order.order_status = OrderStatus.PAID
            self.order.save()
            logger.info('Der Aufrag wurde bei mentoki gespeichert: '
                        '[%s] mit dem Status: [%s]'
                        % (self.order, self.order.order_status))
            self.payment_success = True
        # ----------------------------------------
        # register for courseevent on success
        # ----------------------------------------
            if courseproduct.hasattr('courseevent'):
                # set up courseevent participation
                participation, created =\
                CourseEventParticipation.objects.get_or_create(
                    user=user,
                    courseevent=courseproduct.courseevent)
                if participation:
                    logger.info('participation: [%s] created:[%s]'
                                 % (participation, created))

        # ----------------------------------------
        # react on errors
        # ----------------------------------------
        else:
            if AuthenticationError:
                print "!!!!! ERROR"


            for error in result.errors.deep_errors:
                logger.info('Fehler bei braintree: Code[%s] Nachricht:[%s]'
                             % (error.code, error.message))
            self.transaction.transaction_status = TransactionStatus.FAILED_PAYMENT_DECLINED
            if self.transaction:
                logger.info('transaction there [%s] but no success'
                     % (self.transaction))
                pass
            else:
                message = ""
                for error in result.errors.deep_errors:
                    message += ("CODE: %s MESSAGE: %s \n" %
                    (error.code, error.message))
                self.transaction.braintree_error_details = message
                self.transaction.save()
                logger.info('error during transaction [%s]'
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

