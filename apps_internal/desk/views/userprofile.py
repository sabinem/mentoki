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


class UserProfileView(
    LoginRequiredMixin,
    TemplateView):
    """
    This view shows the users profile with his different roles
    as mentor and as customer
    """
    template_name = 'desk/pages/userprofile.html'

    def get_context_data(self, **kwargs):
        """
        gets the users profile as mentor and customer
        """
        logger.info('[%s] sieht sich sein Profil auf dem Schreibtisch an'
                    % self.request.user)
        context = super(UserProfileView, self).get_context_data(**kwargs)
        user = self.request.user
        context['user'] = user

        # get mentor_profile
        try:
            mentor = MentorsProfile.objects.get(user=user)
            logger.info(' - ist Mentor')
            context['mentor'] = mentor
            productgroups = mentor.productgroups()
            context['productgroups'] = productgroups


        except ObjectDoesNotExist:
            # user is not a mentor
            pass

        return context


