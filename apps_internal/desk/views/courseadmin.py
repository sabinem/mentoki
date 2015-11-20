# coding: utf-8

"""
Entrypoint for updtaing and viewing the users profile
"""
#TODO: update possiblity is missing so far

from __future__ import unicode_literals, absolute_import

from django.views.generic import TemplateView
from django.core.exceptions import ObjectDoesNotExist

from braces.views import LoginRequiredMixin

from apps_accountdata.userprofiles.models.mentor import MentorsProfile

import logging
logger = logging.getLogger('activity.users')


class CourseAdminView(
    LoginRequiredMixin,
    TemplateView):
    """
    This view shows the users profile with his different roles
    as mentor and as customer
    """
    template_name = 'desk/pages/courseadmin.html'

    def get_context_data(self, **kwargs):
        """
        gets the users profile as mentor and customer
        """
        logger.info('[%s] sieht sich seine Produktgruppen auf dem Schreibtisch an'
                    % self.request.user )
        context = super(CourseAdminView, self).get_context_data(**kwargs)
        user = self.request.user
        context['user'] = user

        # get mentor_profile
        try:
            mentor = MentorsProfile.objects.get(user=user)
            logger.info(' - ist Mentor')
            context['mentor'] = mentor
            productgroups = mentor.productgroups()
            logger.info(' - hat Kurse' % productgroups)
            context['productgroups'] = productgroups

        except ObjectDoesNotExist:
            # user is not a mentor
            pass

        return context


