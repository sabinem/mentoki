# coding: utf-8

"""
Entrypoint for updtaing and viewing the users profile
"""
#TODO: update possiblity is missing so far

from __future__ import unicode_literals, absolute_import

from django.views.generic import TemplateView
from django.core.exceptions import ObjectDoesNotExist

from braces.views import LoginRequiredMixin

from allauth.account.models import EmailAddress

from apps_accountdata.userprofiles.models.mentor import MentorsProfile
from apps_customerdata.customer.models.customer import Customer
from apps_customerdata.customer.models.order import Order
from apps_pagedata.public.models import StaticPublicPages

import logging
logger = logging.getLogger('activity.users')


class PageAdminView(
    LoginRequiredMixin,
    TemplateView):
    """
    This view shows the users profile with his different roles
    as mentor and as customer
    """
    template_name = 'desk/pages/pageadmin.html'

    def get_context_data(self, **kwargs):
        """
        gets the users profile as mentor and customer
        """
        logger.info('[%s] sieht sich die Seiten auf dem Schreibtisch an'
                    % self.request.user)
        context = super(PageAdminView, self).get_context_data(**kwargs)
        user = self.request.user
        context['user'] = user

        if user.is_staff:
            pages = StaticPublicPages.objects.all()
            context['pages'] = pages

        print context

        return context