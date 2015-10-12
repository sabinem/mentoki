from __future__ import unicode_literals, absolute_import
import braintree
from django.conf import settings
from django import forms
from django.core.urlresolvers import reverse
from django.views.generic import FormView, TemplateView
import logging
from .models import Customer

logger = logging.getLogger(__name__)


# TODO: use the right environment here. Possible values are:
#       Development, QA, Sandbox and Production.
bt_env = braintree.Environment.Sandbox

# configure the global braintree object:
braintree.Configuration.configure(
    environment=bt_env,
    merchant_id=settings.BRAINTREE['merchant_id'],
    public_key=settings.BRAINTREE['public_key'],
    private_key=settings.BRAINTREE['private_key']
)


class BraintreeForm(forms.Form):
    first_name = forms.CharField(label='First name')
    last_name = forms.CharField(label='Last name')
    amount = forms.CharField(label='Amount')
    payment_method_nonce = forms.CharField()


class PaymentView(FormView):
    """
    This view contains the payment form.
    """

    template_name = 'payment_form.html'
    form_class = BraintreeForm

    def get_context_data(self, **kwargs):
        cx = super(PaymentView, self).get_context_data(**kwargs)
        cx['client_token'] = braintree.ClientToken.generate()
        return cx

    def get_initial(self):
        return {
            'amount': '10.00'
        }

    def get_success_url(self):
        return reverse('payment_success')

    def form_valid(self, form):
        # Collect payment info
        nonce = form.cleaned_data['payment_method_nonce']
        logger.debug('payment method nonce received from: %s'
                     % self.request.user)

        user = self.request.user
        customer = None

        # create a customer
        # use a Customer model if you need to store the address and don't want
        # to do it on the User model.
        # https://developers.braintreepayments.com/javascript+python/reference/response/customer
        if user.is_authenticated():
            if not user.customer:
                # create a customer object
                result = braintree.Customer.create({
                  'first_name': form.cleaned_data('first_name'),
                  'last_name': form.cleaned_data('last_name'),
                  'payment_method_nonce': nonce
                })
                if result.is_success:
                    customer = Customer.objects.create(
                        id=result.customer_id,
                        user=user
                    )
                else:
                    raise Exception('could not create customer. %s' % result)
            else:
                customer = Customer()


        # Prepare the transaction
        # https://developers.braintreepayments.com/javascript+python/reference/request/transaction/sale
        transaction_data = {
            'amount': form.cleaned_data['amount'],
            'payment_method_nonce': nonce,
        }

        if customer and customer.id:
            transaction_data['customer_id'] = customer.id
        else:
            # The customer wanted to check out without registration.
            # TODO: create the customer object form the form fields
            transaction_data['customer'] = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],

            }

        transaction_data['billing'] = {
            'street_address': 'Musterstrasse 3',
            'postal_code': '1234',
            'country_code_alpha2': 'CH',
        }

        # Commit the transaction
        result = braintree.Transaction.sale(transaction_data)

        # TODO: Check if the payment went through

        if not result.is_success:
            logger.warning('Payment Error: %s' % result.message)
            return self.form_invalid(form)

        logger.info('payment processed: %s' % result)
        # TODO: Store transaction info in a database.

        # redirect to thank you page.
        return super(PaymentView, self).form_valid(form)