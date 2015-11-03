# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import RedirectView
from django.shortcuts import get_object_or_404

from braces.views import MessageMixin

from apps_customerdata.customer.models.order import Order
from apps_productdata.mentoki_product.models.courseproduct import CourseProduct
from apps_productdata.mentoki_product.models.courseproductgroup import CourseProductGroup


import logging
logger = logging.getLogger('public.customers')


class CheckoutStartView(
    MessageMixin,
    RedirectView):
    """
    The view serves as a tool to redirect the person who wants to book a
    courseproduct and send him to login and registration first, have him
    confirm his email, before he is brought back to do what he wanted to do.

    His intention is kept in the session and in the next parameter.
    It will be still there after he logs in or signs up, if he uses the
    direct way, that is shown to him for this.

    In case he just have to login, the next parameter is doing the job.
    In case he has to signup and confirm his email first, his intention is
    stored in the session. The signup form writes it into the database from the
    session, when he is first registered and the desk entry point (LOGIN_URL
    from the settings file, redirects him and sets his initial intention back
    during that proccess.

    So if the user signs up with a certain intention to buy a product,
    he is helped through the process of signup and does not have to search
    again, before he finally gets back to his desired purchase.
    """
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        """
        redirects to the login page in case a user is not logged in
        otherwise it uses the session and redirects to where the user
        wanted to go before he was forced to login or register
        :return: redirect_url
        """
        logger.info('%s ruft die Zahlung für %s auf'
                    % (self.kwargs['slug'], self.request.user))

        user = self.request.user

        if self.request.user.is_authenticated():
            # if the user is logged in he may book right away
            # only the product he was after must be determined,
            # since he have had to register in between

            product_url = reverse('checkout:payment', kwargs=kwargs)
            # since the user will be able to checkout now
            if kwargs.has_key('slug'):
                # product is in kwargs

                logger.info(
                    'redirecting to url %s'
                    % product_url)
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
                        return product_url
                    else:
                        self.messages.warning('''Du kannst dieses Produkt nicht buchen,
                            weil es sich mit Kursen überschneidet,
                            die Du bereits gebucht hast. Siehe die Liste unten,
                            welche Kurse für Dich im Angebot sind.''')
                        courseproductgroup = get_object_or_404(
                            CourseProductGroup,
                            course=courseproduct.course)
                        coursegroup_url = reverse('storefront:offer', kwargs={
                            'slug': courseproductgroup.slug
                        })
                        return coursegroup_url
                else:
                    return product_url

            else:
                # product is not defined
                list_url = reverse('storefront:list')
                logger.info(
                    'redirecting to list since product slug was not given %s'
                    % list_url)
                return list_url
        else:
            # message for the anonymous user about why he was thrown back to
            # the login view
            self.messages.info('''Bitte melde Dich an, bevor Du Dich für einen
                               Mentoki-Kurs registrieren kannst''')

            # prepare session in case it takes longer for the person to come
            # back: that will be the case if he has to register first
            next = reverse('checkout:redirect_to_product',
                           kwargs=kwargs)
            self.request.session['next'] = next
            self.request.session['unfinished_checkout'] = True
            self.request.session['unfinished_product_slug'] = self.kwargs['slug']

            # get url to contain a next part that bring the person back here
            # right after login
            from urlparse import urljoin
            login_url = reverse('account_login')
            next_url = '?next=%s' % self.request.path
            login_and_back_url = urljoin(login_url, next_url)
            return login_and_back_url

