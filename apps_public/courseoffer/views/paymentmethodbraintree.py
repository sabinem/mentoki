# coding: utf-8

"""
Paymill Integration Payment Form
"""

from __future__ import unicode_literals, absolute_import

from django.conf import settings
from django.core.urlresolvers import reverse
from django.views.generic import FormView, TemplateView
from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as _
from mentoki.settings import LOGIN_REDIRECT_URL
from allauth.account.decorators import verified_email_required
from django.core.exceptions import ObjectDoesNotExist

from braces.views import LoginRequiredMixin, MessageMixin, UserPassesTestMixin

import paymill

from apps_customerdata.customer.models import Customer
from apps_data.courseevent.models.courseevent import CourseEvent
from apps_core.core.mixins import TemplateMixin

from .info import CourseEventProductMixin

import logging
logger = logging.getLogger(__name__)


from apps_customerdata.mentoki_product.models.courseevent \
    import CourseEventProduct


class PaymillForm(forms.Form):
    token = forms.CharField(widget=forms.HiddenInput())


class PaymentMethodView(
    CourseEventProductMixin,
    FormView):
    """
    Payment of courseevent
    """
    form_class = PaymillForm

    template_name = 'courseoffer/pages/paymentdata.html'

    def get_context_data(self, **kwargs):
        context = super(PaymentMethodView, self).get_context_data(**kwargs)

        user = self.request.user
        context['PAYMILL_PUBLIC_KEY'] = settings.PAYMILL['public_key']
        paymill_context = \
            paymill.PaymillContext(settings.PAYMILL['private_key']);
        logger.info("[%s] [Courseeventproduct Payment]"
                    % (user))

        try:
            customer = Customer.objects.get(user=user)
            logger.info("[%s] [Courseeventproduct Payment]: customer exists: %s %s"
                    % (user, customer, customer.paymill_client))
            client_service = paymill_context.get_client_service()
            client = customer.paymill_id
            paymill_client =  client_service.detail(client)
            import ipdb; ipdb.set_trace()
        except ObjectDoesNotExist:
            logger.info("[%s] [Courseeventproduct Payment]: customer does not exists"
                    % (user))
            client_service = paymill_context.get_client_service()
            paymill_client =  client_service.create(email=user.email)
            logger.info("[%s] [Courseeventproduct Payment]: paymill client created: %s"
                    % (user, paymill_client.id))
            paymill_client =  client_service.create(paymill_client)
            logger.info("[%s] [Courseeventproduct Payment]: paymill client found: %s"
                    % (paymill_client.id))

            #customer.create(paymill_id=paymill_client.client)
            customer = Customer.objects.create(

                )
            customer = Customer()
            print paymill_client
        return context



    def get_success_url(self):
        url = None
        if self.success:
            url = reverse('payment:success')
        else:
            url = reverse('payment:failed')
        return url

    def form_valid(self, form):
        # check for customerdata
        user = self.request.user
        if user.is_authenticated():
            try:
                customer = get_object_or_404(Customer, user=self.request.user)
            except ObjectDoesNotExist:
                customer = Customer.objects.create()

        return context


        # Change payment status and jump to success_url or failure_url

        token = form.cleaned_data['token']
        print "token: %s" % token
        #logger.info("[%s] [Zahlung %s %s]:" % (
        #    self.object.product,
        #    self.object.id,
        #    self.object.title,
        #    mail_distributor))
        paymill_context = paymill.PaymillContext(settings.PAYMILL['private_key'])

        payment_service = paymill_context.get_payment_service()
        payment_with_token = payment_service.create(
            token=token
        )
        payment_with_token_and_client = payment_service.create(
            token='098f6bcd4621d373cade4e832627b4f6',
            client_id='client_33baaf3ee3251b083420'
        )

        amount = 4200
        currency = 'EUR'
        transaction_service = paymill_context.get_transaction_service()
        transaction_with_token = transaction_service.create_with_token(
            token=token,
            amount=4200, currency='EUR',
            description='Test Transaction',
            fee_amount=4200,
            fee_payment_id='pay_3af44644dd6d25c820a8',
            fee_currency='EUR'
        )

        #transaction = pmill.transact(amount, payment=card, currency=currency)

        transaction = True
        if transaction:
            self.success = True
            if not self.payment.on_success():
                # This method returns if payment was fully paid
                # if it is not, we should alert user that payment was not successfully ended anyway
                self.success = False
        else:
            self.success = False
            self.payment.on_failure()
        return super(PaymentView, self).form_valid(form)


class PaymentSuccessView(TemplateView):
    """
    This view is called if the payment has been successful.
    """
    template_name = 'transaction/pages/payment_sucessful.html'


class PaymentFailedView(TemplateView):
    """
    This view is called if the payment has been declined.
    """
    template_name = 'transaction/pages/payment_failed.html'