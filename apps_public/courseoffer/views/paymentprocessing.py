# coding: utf-8

from __future__ import unicode_literals, absolute_import
"""
Payrexx payment processing
"""

from apps_customerdata.invoice.models.invoice import Invoice

from django.conf import settings
from django import forms
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.views.generic import FormView, TemplateView
from django.core.exceptions import ObjectDoesNotExist

import logging
logger = logging.getLogger(__name__)

from apps_customerdata.mentoki_product.models.courseevent \
    import CourseEventProduct
from apps_core.email.utils.invoice import send_invoice
from .info import CourseEventProductMixin


class PaymentEmailForm(forms.Form):
    """
    Payment Form uses Braintrees Drop In
    """
    customer_email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()


class PaymentEmailView(
    FormView,
    CourseEventProductMixin,
    ):
    """
    This view contains the payment form.
    """
    template_name = 'courseoffer/pages/payment_email_form.html'
    form_class = PaymentEmailForm

    def get_context_data(self, **kwargs):
        """
        gets the product and the braintree client token
        """
        context = super(PaymentEmailView, self).get_context_data(**kwargs)
        context['url_name'] = self.request.resolver_match.url_name

        courseeventproduct = get_object_or_404(CourseEventProduct,pk=self.kwargs['pk'])
        context['courseeventproduct'] = courseeventproduct
        logger.debug('payment started for: %s'
                     % (courseeventproduct))

        return context

    def form_valid(self, form):
        """
        handles the transaction and the customer identification
        """
        self.product = get_object_or_404(CourseEventProduct, pk=self.kwargs['pk'])
        self.invoice = Invoice.objects.create(
            product=self.product, email=form.cleaned_data['customer_email'],
            payrexx_tld=2, first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name']
        )

        #send_email_to_customer
        print "invoice after creating %s" % self.invoice

        email_send = send_invoice(
                invoice=self.invoice,
                module=self.__module__
            )
        print email_send


        return super(PaymentEmailView, self).form_valid(form)

    def get_success_url(self):
        """
        redirects to the success page after paying
        """
        return reverse('courseoffer:payment_success', kwargs={'slug': self.kwargs['slug'],
                                                              'invoice_nr': self.invoice.invoice_nr
                                                              })


class SuccessView(
    CourseEventProductMixin,
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
        context['invoice'] = get_object_or_404(Invoice, invoice_nr=self.kwargs['invoice_nr'])
        print "========= HALLO ============="
        print context
        return context


