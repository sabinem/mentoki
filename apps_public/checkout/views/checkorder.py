# coding: utf-8

"""
Checkorder: This view takes up the order, when a student wants to book a
courseproduct. The student is supposed to login, if he is already a registered
user. Otherwise the order is taking in preparation of him being registered after
the order was processed.
"""

from __future__ import unicode_literals, absolute_import

from django import forms
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import FormView
from django.core.exceptions import ObjectDoesNotExist
from django.forms import ValidationError

from braces.views import MessageMixin
from braces.views import LoginRequiredMixin, UserPassesTestMixin

import logging
logger = logging.getLogger(__name__)

from apps_customerdata.customer.models.order import Order
from apps_customerdata.customer.models.customer import Customer
from apps_productdata.mentoki_product.models.courseproduct \
    import CourseProduct
from apps_productdata.mentoki_product.models.courseproductgroup import \
    CourseProductGroup

# TODO import User from settings instead ?
from accounts.models import User
from django.conf import settings


from allauth.account.decorators import verified_email_required


class CheckOrderForm(forms.ModelForm):
    """
    Check Order: the first step when checking out.
    A temporary order is initiated
    """
    class Meta:
        model = Order
        fields = ('first_name', 'last_name',
                  'username',
                  'email')

    def __init__(self, *args, **kwargs):
        """
        Gets the product and the user
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
            if not self.cleaned_data['email'] \
                or not self.cleaned_data['first_name'] \
                or not self.cleaned_data['last_name'] \
                or not self.cleaned_data['username']:
                raise ValidationError('Bitte Teilnehmerdaten vollständig ausfüllen.')

            # check whether user/email exists already
            email = self.cleaned_data['email']
            try:
                User.objects.get(email=email)
                raise ValidationError('''Diese Email-Adresse ist schon bei Mentoki registriert.
                                      Melde Dich bitte an, bevor Du den Kurs buchen kannst.''')
            except ObjectDoesNotExist:
                pass
            # check whether username exists already
            username = self.cleaned_data['username']
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
    #LoginRequiredMixin,
    MessageMixin,
    FormView):
    """
    This view checks the participant data and whether it is possible for a participant
    to buy the product / register for a course. If everything is fine it establishes an
    initial order object, that will still be there in case the payment does not
    go through. It can be used for example to get back to the customer and assist him with the
    payment process. Some of our products will be expensive, so this does make sense.

    Later on preorders might also be used to take an interest in a class into account.
    The person might be contacted in case the class opens for registration.
    """
    template_name = 'checkout/pages/checkorder.html'
    form_class = CheckOrderForm

    def get_context_data(self, **kwargs):
        """
        gets the product data
        """
        context = super(CheckOrderView, self).get_context_data(**kwargs)
        courseproduct_slug = self.kwargs['slug']

        try:
            # product data should be deductable from the url
            self.courseproduct = CourseProduct.objects.get(
                slug=courseproduct_slug)
            self.courseproductgroup = CourseProductGroup.objects.get(
                course=self.courseproduct.course)
            context['courseproductgroup'] = self.courseproductgroup
            context['courseproduct'] = self.courseproduct

        except ObjectDoesNotExist:
            # if any of the product data was not found
            # it is a programming error and will be reported
            logger.error('coursproduct was not found with slug: %s'
                     % courseproduct_slug)
            # the user will be sent to an error page
            return reverse('checkout:checkout_failed',
                       kwargs={'slug': self.kwargs['slug']})

        context['user'] = self.request.user
        logger.debug('-------------- payment started for: %s %s'
                     % (self.request.user, self.courseproduct))
        return context


    def get_form_kwargs(self):
        """
        save the user and the product data for the form, to check
        whether there is already an order for that combination.
        """
        user = self.request.user
        courseproduct_slug = self.kwargs['slug']

        kwargs = super(CheckOrderView, self).get_form_kwargs()

        kwargs['user']= user
        kwargs['courseproduct_slug'] = courseproduct_slug

        return kwargs

    def form_valid(self, form):
        """
        creates the order
        """
        # the product was determined in the form init
        courseproduct = form.courseproduct

        # user
        user = self.request.user

        if user.is_authenticated():
            if user.hasattr('customer'):
                customer = user.customer
            else:
                # create customer:
                customer = Customer.objects.create(
                    user=user,
                )
        else:
            # customer will be created later after the transaction
            # along with the user
            customer = None

        # create the initial order
        self.object = Order.objects.create(
            #product, that is ordered
            courseproduct=courseproduct,
            #sales price at the time of order
            amount=courseproduct.amount,
            currency=courseproduct.currency,
            #customer datafrom the form
            email=form.cleaned_data['email'],
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            username=form.cleaned_data['username'],
        )

        return super(CheckOrderView, self).form_valid(form)

    def get_success_url(self):
        """
        redirects to the next step
        """
        return reverse('checkout:payment',
                       kwargs={'slug': self.kwargs['slug'],
                               'temporder_pk':self.object.pk})
