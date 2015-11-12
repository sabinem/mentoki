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
from django.utils.encoding import smart_str
from django.views.decorators.cache import cache_control

from django.conf import settings

from braces.views import MessageMixin, UserPassesTestMixin, FormMessagesMixin

import braintree

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
logger = logging.getLogger('activity.payments')
logger_sentry = logging.getLogger('sentry.payments')


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
    :return: redirects to a "success" page after successful payment or to
        a failure page in case an error happened
    """
    template_name = 'checkout/pages/payment_form.html'
    form_class = PaymentForm

    #@cache_control(no_cache=True, must_revalidate=True)
    @method_decorator(verified_email_required)
    def dispatch(self, request, *args, **kwargs):
        """
        The users email needs to be verified before booking a course
        (@method_decorator(verified_email_required).
        Also the back key should not bring back the payment form, once the
        payment is done (@cache_control).
        """
        logger.info('-------------- neuer Zahlungsaufruf')
        return super(PaymentView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        """
        prepares the payment by creating all necessary payment objects
        such as
         - the customer
         - the order (for the customer buying the product)
         - the transaction (this try to pay the order)

        a braintree token must be created to open communication with the
        payment provider
        the method to create the token gets the following
        arguments:
        - braintree id of the customer
        - braintree_merchant_id according to the currency of the payment
        """
        # user from request
        user=self.request.user

        # courseproduct, that is to be bought
        self.courseproduct = get_object_or_404(
            CourseProduct,
            slug=self.kwargs['slug'])
        self.amount = self.courseproduct.sales_price
        self.currency = self.courseproduct.currency
        logger.info('Zahlung gestartet für Benutzer [%s] Produkt [%s]'
                    % (user, self.courseproduct))
        self.courseproductgroup = get_object_or_404(
            CourseProductGroup,
            course=self.courseproduct.course)
        logger.info(
            'Die Produktdaten: Normalpreis:[%s], Rabattpreis:[%s],'
            ' Währung:[%s]'
                 % (self.courseproduct.price,
                    self.amount,
                    self.courseproduct.get_currency_display()))

        # get or create customer
        self.customer, created = Customer.objects.get_or_create(
            user=user)
        if created:
            logger.info('Der Kunde [%s] wurde bei mentoki neu angelegt mit der '
                         'braintree id [%s]'
                         % (self.customer,
                            self.customer.braintree_customer_id))
        else:
            logger.info('Der Kunde [%s] mit der '
                         'braintree id [%s] wurde bei mentoki gefunden'
                         % (self.customer,
                            self.customer.braintree_customer_id))

        # get or open order
        self.order, created = Order.objects.get_or_create(
            courseproduct=self.courseproduct,
            customer=self.customer,
            defaults={
                'amount':self.amount,
                'currency':self.courseproduct.currency,
                'email':user.email,
                'first_name':user.first_name,
                'last_name':user.last_name}
        )
        if created:
            logger.info('Ein Auftrag [%s] wurde bei neu mentoki angelegt.'
                         % (self.order))
        else:
            # Error case: order is already paid (might happen if customer works
            # on parallel screens?)
            logger.info('Es gab schon einen Auftrag [%s] im Status [%s] zu '
                         'dieser Buchung, er wurde fürs Update vorbereitet.'
                         % (self.order, self.order.order_status))
            if self.order.order_status == OrderStatus.PAID:
                logger.error_sentry('Versuch die Order [%s] doppelt zu bezahlen:'
                     'Transaktion[%s]'
                      % (self.order, self.transaction))
                self.messages.error('''Der Kurs wurde bereits gebucht und
                bezahlt. Er kann nicht doppelt bezahlt werden.''')
                logger_sentry.error('Kunde hat versucht doppelt zu bezahlen.'
                    'Transaktion: [%s]:' % self.transaction)
                return self.redirect_on_error(**kwargs)

        # create transaction
        self.transaction = Transaction.objects.create(
            amount=self.amount,
            braintree_amount=str(self.amount),
            currency=self.currency,
            customer=self.customer,
            order=self.order,
            braintree_customer_id = self.customer.braintree_customer_id,
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name,
            course=self.courseproduct.course
        )
        # set transaction merchant key according to currency
        if self.currency == Currency.CHF:
            self.transaction.braintree_merchant_account_id = \
                settings.BRAINTREE['merchant_account_id_chf']
        elif self.currency == Currency.EUR:
            self.transaction.braintree_merchant_account_id = \
                settings.BRAINTREE['merchant_account_id_eur']
        else:
            raise IntegrityError(
                'Unbekannte Währung [%s] bei Kursprodukt:[%s]' %
                (self.currency, self.courseproduct))
        self.transaction.save()
        logger.info('Eine Transaktion [%s] wurde bei Mentoki angelegt'
                     % (self.transaction))

        # create token for braintree communication
        self.token=None
        braintree_token_args = {}
        braintree_token_args['customer_id'] \
            = self.transaction.braintree_customer_id
        braintree_token_args['merchant_account_id'] = \
            self.transaction.braintree_merchant_account_id
        try:
            logger.info('Zur Generierung des Payment Tokens für braintree'
                         'werden folgende Argumente mitgegeben:[%s]'
                         % braintree_token_args)
            self.token = braintree.ClientToken.generate(
                braintree_token_args)
            logger.info('Das Token wurde generiert')
        except BraintreeError as ex:
            logger_sentry.error('braintree authentication error [%s] erhalten'
                         % ex)
            self.messages.error('''Entschuldigen Sie bitte. Beim
            Verbindungsaufbau zum Zahlungsanbieter ist ein Fehler aufgetreten.
            Wir haben aber Ihren Buchungswunsch aufgenommen
            und werden uns in Kürze mit Ihnen in Verbindung setzen.''')
            self.transaction.error_code = \
                TransactionErrorCode.BRAINTREE_CONNECTION_ERROR
            self.transaction.error_details = ex.__class__.__name__
            self.transaction.save()
            return self.redirect_on_error()

        # transaction is memorized in the session for the post method
        self.request.session['transaction_id'] = self.transaction.id
        return super(PaymentView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        """
        the context contains the payment nounce for the communication
        with braintree and also the productdata
        :param the view (self)
        :return: context
        """
        context = super(PaymentView, self).get_context_data(**kwargs)
        context['amount'] = self.amount
        context['courseproductgroup'] = self.courseproductgroup
        context['courseproduct'] = self.courseproduct
        context['client_token'] = self.token
        return context

    def redirect_on_error(self):
        """
        redirects on error to a error page
        :return: response that redirects to the error page
        """
        logger.info('im error redirect.')
        return HttpResponseRedirect(reverse(
            'checkout:payment_failure',
            kwargs={'order_pk':self.order.pk,
                    'slug':self.kwargs['slug']}))


    def post(self, request, *args, **kwargs):
        """
        Handles POST requests: the payment data are recovered from the
        transaction id that has been memorized in the session.
        """
        try:
            self.transaction = \
                Transaction.objects.get(
                    id=self.request.session['transaction_id'])
            transaction = self.transaction
            self.order = Order.objects.get(id=self.transaction.order_id)
            self.customer = Customer.objects.get(id= self.order.customer_id)
            self.courseproduct = self.order.courseproduct
            self.amount = self.transaction.amount
            self.currency = self.transaction.currency
            self.merchant_account_id = \
                self.transaction.braintree_merchant_account_id

        except ObjectDoesNotExist:

            logger_sentry.error('Zahlungsobjekt wurde nicht gefunden zur '
                'Transaktionsnummer [%s] (Transaktion, Order oder Kunde.'
                % self.request.session['transaction_id'])
            self.messages.error('''Entschuldigen Sie bitte. Bei der Zahlung
            ist ein Fehler aufgetreten. Bitte kontaktieren Sie uns.''')
            return self.redirect_on_error()
        # user
        self.user = self.request.user
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


    def form_valid(self, form):
        """
        Now the actual payment takes place.
        """
        # get the payment nonce from the form
        nonce = form.cleaned_data['payment_method_nonce']
        self.success = False
        logger.info('Das Token wurde gefunden.')

        # prepare braintree transaction

        transaction_data = {}
        transaction_data['amount'] = self.amount
        transaction_data['options'] = {
                    'submit_for_settlement': True,
                    'store_in_vault_on_success': True,
                }
        transaction_data['order_id'] = self.order.id

        # customer data will be created along with the transaction

        if not self.transaction.braintree_customer_id:
            transaction_data['customer'] = {
                            "first_name": self.transaction.first_name,
                            "last_name": self.transaction.last_name,
                            "email": self.transaction.email
                      }
            transaction_data['merchant_account_id'] = \
                self.merchant_account_id
        logger.info('Braintree Transaktion mit folgendem Input (Token wird '
                    'nicht angezeigt): [%s]'
                     % (transaction_data))
        transaction_data['payment_method_nonce'] = nonce
        result = braintree.Transaction.sale(transaction_data)

        # store transaction result

        if result.transaction:

            # update customer who is now registered at braintree
            if (not self.customer.braintree_customer_id and
                result.transaction.customer['id']):
                self.customer.braintree_customer_id = \
                    result.transaction.customer['id']
                self.customer.save()
                logger.info('Braintree-Kundennr gespeichert): [%s]'
                             % (result.transaction.customer['id']))
            # update transaction
            self.transaction.braintree_transaction_id = \
                result.transaction.id
            self.transaction.success = result.is_success
            self.transaction.braintree_amount = result.transaction.amount
            if result.transaction.customer['id']:
                self.transaction.braintree_customer_id = \
                    result.transaction.customer['id']
            self.transaction.braintree_merchant_account_id \
                = result.transaction.merchant_account_id
            self.transaction.braintree_transaction_id = result.transaction.id
            if result.transaction.credit_card['token']:
                self.transaction.braintree_payment_token = \
                    result.transaction.credit_card['token']

            if hasattr(result.transaction, 'braintree_processor_response_code'):
                self.transaction.braintree_processor_response_code = \
                    result.transaction.processor_response_code
                self.transaction.braintree_processor_response_text = \
                    result.transaction.processor_response_text
                self.transaction.error_code = \
                    TransactionErrorCode.PAYMENT_DECLINED

        if hasattr(result, 'message'):
            self.transaction.braintree_error_message = \
                result.message

        if hasattr(result, 'errors'):
            self.transaction.error_code = \
                TransactionErrorCode.FAILED_SYSTEMERROR
            message = ""
            for error in result.errors.deep_errors:
                message += ("ERROR: %s CODE: %s MESSAGE: %s \n" %
                (error.__class__.__name__, error.code, error.message))
            self.transaction.braintree_error_details = smart_str(message)

        self.transaction.save()

        # react on transaction

        # transaction had success:
        if result.is_success:
            self.success = True
            # log success

            logger_sentry.info('Die Transaktion hatte Erfolg. Diese Transaction'
                    ' kam von braintree zurück: [%s]. ' %
                    braintree.transaction)

            # update order

            self.order.order_status = OrderStatus.PAID
            self.order.save()
            logger.info('Der Aufrag wurde upgedated: '
                        '[%s] mit dem Status: [%s]'
                        % (self.order, self.order.order_status))

            # register participant for courseevent

            if getattr(self.courseproduct, 'courseevent'):
                participation, created =\
                CourseEventParticipation.objects.get_or_create(
                    user=self.user,
                    courseevent=self.courseproduct.courseevent)
                if participation:
                    logger.info('participation: [%s] created:[%s]'
                                 % (participation, created))

        # transaction had not success: payment was declined
        else:

            #client bank failed

            if self.transaction.error_code == \
                    TransactionErrorCode.PAYMENT_DECLINED:

                #update order

                self.order.order_status = OrderStatus.DECLINED
                self.order.save()

                # log error

                logger_sentry.error(
                    'Die Zahlung des Auftrags [%s] wurde abgelehnt:'
                    'braintree Nachricht [%s] Code: [%s]'
                    % (self.order,
                       self.transaction.braintree_processor_response_code,
                       self.transaction.braintree_processor_response_text))

                # message to user

                self.messages.error('''Leider ist bei Ihrer Zahlung ein Fehler
                    aufgetreten. Ihre Bank hat die Zahlung abgelehnt. Nehmen
                    Sie gerne Kontakt mit uns auf in dieser Sache.''')
                return self.redirect_on_error()

            else:

                #update order

                self.order.order_status = OrderStatus.ERROR_DURING_PAYMENT
                self.order.save()

                #log error

                logger_sentry.error('Es gab einen Fehler beim Aufruf von braintree'
                    ' Die Fehlernachricht lautet: [%s]' %
                    result.message)

                # message to user

                self.messages.error('''Es gab auf unserer Seite einen Fehler
                    bei Ihrer Zahlung. Wir kümmern uns darum und kontaktieren
                    Sie sobald als möglich. Ihren Buchungswunsch haben wir
                    gespeichert.''')
                return self.redirect_on_error()

        return super(PaymentView, self).form_valid(form)

    def get_success_url(self):
        """
        redirects to success page in case of payment success
        :return: url
        """
        url = reverse('checkout:payment_success',
                      kwargs={'order_pk': self.order.pk,
                              'slug': self.kwargs['slug']})
        logger.info('in get success_url %s' % url)
        return url


