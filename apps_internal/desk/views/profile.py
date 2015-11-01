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


class DeskProfileView(
    LoginRequiredMixin,
    TemplateView):
    """
    This view shows the users profile with his different roles
    as mentor and as customer
    """
    template_name = 'desk/pages/profile.html'

    def get_context_data(self, **kwargs):
        """
        gets the users profile as mentor and customer
        """
        context = super(DeskProfileView, self).get_context_data(**kwargs)
        user = self.request.user
        context['user'] = user

        # get mentor_profile
        try:
            mentor = MentorsProfile.objects.get(user=user)
            context['mentor'] = mentor
        except ObjectDoesNotExist:
            # user is not a mentor
            pass

        try:
            customer = Customer.objects.get(user=user)
            context['customer'] = customer
        except ObjectDoesNotExist:
            # user is not a customer
            pass

        try:
            context['email'] = EmailAddress.objects.get(user=user)
        except ObjectDoesNotExist:
            # not yet verified, may be old user, before allauth was implemented
            pass

        return context


