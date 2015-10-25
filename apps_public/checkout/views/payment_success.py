# coding: utf-8

"""
Braintree Integration Payment Form
"""

from __future__ import unicode_literals, absolute_import

from django.shortcuts import get_object_or_404
from django.views.generic import FormView, TemplateView
from django.contrib.auth.forms import PasswordResetForm

from apps_productdata.mentoki_product.models.courseproduct import \
    CourseProduct
from apps_productdata.mentoki_product.models.courseproductgroup import \
    CourseProductGroup
from apps_customerdata.customer.models.order import Order

import logging
logger = logging.getLogger(__name__)


class SuccessView(
    TemplateView):
    """
    This view is called if the payment has been successful. This is using:
    https://github.com/django/django/blob/master/django/contrib/auth/forms.py

    class PasswordResetForm()
    def save(self, domain_override=None,
             subject_template_name='registration/password_reset_subject.txt',
             email_template_name='registration/password_reset_email.html',
             use_https=False, token_generator=default_token_generator,
             from_email=None, request=None, html_email_template_name=None,
             extra_email_context=None):
    """
    #TODO: better set email templates for password reset

    template_name = 'checkout/pages/payment_sucessful.html'

    def get_context_data(self, **kwargs):
        """
        gets the product and the braintree client token
        """
        context = super(SuccessView, self).get_context_data(**kwargs)

        order = get_object_or_404(
            Order,
            pk=self.kwargs['order_pk'])
        #TODO: 404 ersetzen durch Fehlerseite + Fehlermeldung an Sentry
        # log.error bei Sentry einstellen
        # log.exception gibt stack trace mit, geht nur in except block

        context['order'] = order

        courseproduct = get_object_or_404(CourseProduct, slug=self.kwargs['slug'])
        context['courseproduct'] = courseproduct
        context['courseproductgroup'] = get_object_or_404(CourseProductGroup,
                                               course=courseproduct.course)
        if not self.request.user.is_authenticated():
            newuser = order.customer.user
            context['newuser'] = newuser
            form = PasswordResetForm({'email':newuser.email})
            form.is_valid()

            form.save()
        return context