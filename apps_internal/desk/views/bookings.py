# coding: utf-8

"""
show booked courses with paid amount
"""

from __future__ import unicode_literals, absolute_import

from django.views.generic import TemplateView
from django.core.exceptions import ObjectDoesNotExist

from braces.views import LoginRequiredMixin

from apps_accountdata.userprofiles.models.mentor import MentorsProfile
from apps_customerdata.customer.models.customer import Customer
from apps_customerdata.customer.models.order import Order
from apps_pagedata.public.models import StaticPublicPages

import logging
logger = logging.getLogger('activity.users')


class BookingsView(
    LoginRequiredMixin,
    TemplateView):
    """
    This view shows the users profile with his different roles
    as mentor and as customer
    """
    template_name = 'desk/pages/bookings.html'

    def get_context_data(self, **kwargs):
        """
        gets the users profile as mentor and customer
        """
        logger.info('[%s] sieht sich sein Profil auf dem Schreibtisch an'
                    % self.request.user)
        context = super(BookingsView, self).get_context_data(**kwargs)
        user = self.request.user
        context['user'] = user

        try:
            customer = Customer.objects.get(user=user)
            context['customer'] = customer
            logger.info(' - ist Kunde :[%s]'
                    % user.customer)
            orders = Order.objects.by_customer_started_to_pay(customer=customer)
            logger.info(' - hat Aufträge')
            context['orders'] = orders
            for order in orders:
                print order.courseproduct.courseevent
        except ObjectDoesNotExist:
            # user is not a customer
            pass

        return context
