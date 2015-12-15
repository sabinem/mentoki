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
from apps_productdata.mentoki_product.models.courseproductgroup import \
    CourseProductGroup, CourseProductGroupField
from apps_pagedata.public.models import StaticPublicPages

import logging
logger = logging.getLogger('activity.users')


class CourseAdminView(
    LoginRequiredMixin,
    TemplateView):
    """
    This view shows the users profile with his different roles
    as mentor and as customer
    """
    template_name = 'desk/pages/textadmin.html'

    def get_context_data(self, **kwargs):
        """
        gets the users profile as mentor and customer
        """
        logger.info('[%s] sieht sich seine Produktgruppen auf dem Schreibtisch an'
                    % self.request.user )
        context = super(CourseAdminView, self).get_context_data(**kwargs)
        user = self.request.user
        context['user'] = user

        if user.is_superuser:
            productgroups = CourseProductGroup.objects.published()
            context['productgroups'] = productgroups

            list=[]
            for group in productgroups:
                groupfields = {'group': group }
                fields = CourseProductGroupField.objects.filter(courseproductgroup=group)
                groupfields['field_list'] = fields
                list.append(groupfields)
            context['courselist'] = list
            context['staticpublicpages'] = StaticPublicPages.objects.all()
            context['mentors'] = MentorsProfile.objects.all()

        return context


