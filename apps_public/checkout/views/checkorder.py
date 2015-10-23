# coding: utf-8

"""
Checkorder
"""

from __future__ import unicode_literals, absolute_import

from django import forms
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.views.generic import FormView
from django.core.exceptions import ObjectDoesNotExist
from django.forms import ValidationError
from django.http import HttpResponseRedirect

from django.conf import settings

import logging
logger = logging.getLogger(__name__)

from apps_customerdata.customer.models.temporder import TempOrder
from apps_customerdata.customer.models.order import Order

from apps_productdata.mentoki_product.models.courseproduct \
    import CourseProduct
from apps_productdata.mentoki_product.models.courseproductgroup import \
    CourseProductGroup

# TODO import User from settings instead ?
from accounts.models import User


class CheckOrderForm(forms.ModelForm):
    """
    Check Order: the first step when checking out.
    A temporary order is initiated
    """
    class Meta:
        model = TempOrder
        fields = ('participant_first_name', 'participant_last_name',
                  'participant_username',
                  'participant_email')

    def __init__(self, *args, **kwargs):
        """
        The init gets the product and the user
        """
        # get product
        courseproduct_slug = kwargs.pop('courseproduct_slug', None)
        self.courseproduct = get_object_or_404(CourseProduct, slug=courseproduct_slug)
        # get user if logged in
        self.user = kwargs.pop('user', None)
        super(CheckOrderForm, self).__init__(*args, **kwargs)

    def clean(self):
        """
        This form is for entering the participant information for anonymous users
        A registered user must login in order to be able to book a course.
        The email is used as an identifier for users. So if an anounymous user
        tries to register with a known email, he is asked to log in. This form
        is only shown to anonymous users.

        It also checks for registered user whether an order for that product already
        exists, since most products can only be bought once.
        """
        # for new users check the pariticipant data
        if not self.user.is_authenticated():
            # check participant data
            if not self.cleaned_data['participant_email'] \
                or not self.cleaned_data['participant_first_name'] \
                or not self.cleaned_data['participant_last_name'] \
                or not self.cleaned_data['participant_username']:
                raise ValidationError('Bitte Teilnehmerdaten vollständig ausfüllen.')

            # check whether user/email exists already
            email = self.cleaned_data['participant_email']
            try:
                User.objects.get(email=email)
                raise ValidationError('''Diese Email-Adresse ist schon bei Mentoki registriert.
                                      Melde Dich bitte an, bevor Du den Kurs buchen kannst.''')
            except ObjectDoesNotExist:
                pass
            # check whether username exists already
            username = self.cleaned_data['participant_username']
            try:
                User.objects.get(username=username)
                raise ValidationError('''Diesen Benutzername gibt es schon.
                                      Suche Dir bitte einen anderen Namen aus.''')
            except ObjectDoesNotExist:
                pass

        # for registered users check whether the user already ordered and paid for the product.

        if self.user.is_authenticated():
            try:
                Order.objects.get(courseproduct=self.courseproduct,
                                  customer=self.user.customer)
                raise ValidationError('''Du bist bereits für diesen Kurs angemeldet. Eine Doppelbuchung
                ist nicht möglich.''')
            except ObjectDoesNotExist:
                # everything fine with this order, proceed
                pass
        return self.cleaned_data


class CheckOrderView(
    FormView):
    """
    This view checks the participant data and whether it is possible for a participant
    to buy the product / register for a course. If everything is fine it establishes a
    temporary order object, that will still be there in case the payment does not
    go through. It can be used for example to get back to the customer and assist him with the
    payment process. Some of our products will be expensive, so this does make sense.

    Later on preorders might also be used to take an interest in a class into account.
    The person might be contacted in case the class opens for registration.
    """
    template_name = 'checkout/pages/checkorder.html'
    form_class = CheckOrderForm

    def get_context_data(self, **kwargs):
        """
        gets the product data and the braintree client token
        """
        context = super(CheckOrderView, self).get_context_data(**kwargs)

        self.courseproduct = get_object_or_404(CourseProduct, slug=self.kwargs['slug'])
        self.courseproductgroup = get_object_or_404(CourseProductGroup, course=self.courseproduct.course)
        context['courseproductgroup'] = self.courseproductgroup
        context['courseproduct'] = self.courseproduct
        context['user'] = self.request.user
        logger.debug('-------------- payment started for: %s %s'
                     % (self.request.user, self.courseproduct))
        return context


    def get_form_kwargs(self):
        """
        save the user and the product data for the form, to check
        wether there is already an order for that combination.
        """
        user = self.request.user
        courseproduct_slug = self.kwargs['slug']
        kwargs = super(CheckOrderView, self).get_form_kwargs()
        kwargs['user']= user
        kwargs['courseproduct_slug'] = courseproduct_slug
        return kwargs

    def form_valid(self, form):
        """
        handles the transaction and the customer identification
        """
        self.object = TempOrder.objects.create(
            courseproduct=form.courseproduct,
            user=form.user,
            participant_first_name=form.cleaned_data['participant_first_name'],
            participant_last_name=form.cleaned_data['participant_last_name'],
            participant_username=form.cleaned_data['participant_username'],
            participant_email=form.cleaned_data['participant_email'],
        )
        return super(CheckOrderView, self).form_valid(form)

    def get_success_url(self):
        """
        redirects to the next step
        """
        return reverse('checkout:payment',
                       kwargs={'slug': self.kwargs['slug'],
                               'temporder_pk':self.object.pk})
