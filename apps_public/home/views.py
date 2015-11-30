# -*- coding: utf-8 -*-

"""
Public pages that describe mentoki. Most of these pages are build dynamically
with text that is fetched from the database.
"""

from __future__ import unicode_literals

from django.views.generic import TemplateView, DetailView

from apps_accountdata.userprofiles.models.mentor import MentorsProfile
from apps_productdata.mentoki_product.models.courseproductgroup import CourseProductGroup
from apps_pagedata.public.models import StaticPublicPages

import logging
logger = logging.getLogger('public.dataintegrity')


class HomePageView(TemplateView):
    """
    Homepage
    """
    template_name = "home/pages/homepage.html"


class PublicPageView(
    DetailView):
    """
    diverse public pages, which text that is taken from the database
    """
    model = StaticPublicPages
    template_name = "home/pages/publicpage.html"
    context_object_name = 'pagedata'


class MentorsListView(TemplateView):
    """
    List of all of Mentokis mentors.
    """
    template_name = "home/pages/mentors.html"

    def get_context_data(self, **kwargs):
        """
        in: no arguments
        out: context that provides all mentors from the database
        """
        context = super(MentorsListView, self).get_context_data()

        mentors = MentorsProfile.objects.mentors_all()
        context['mentors'] = mentors
        return context


class MentorsPageView(DetailView):
    """
    One mentor is displayed in detail along with his courses.
    in: slug of the mentor
    out: context of mentor and his courseproducts
    """
    models = MentorsProfile
    context_object_name = 'mentor'
    template_name = "home/pages/mentor.html"

    def get_queryset(self):
        ""
        return MentorsProfile.objects.filter(slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(MentorsPageView, self).get_context_data()
        mentor = context['mentor']
        context['courseproductgroups'] = \
            CourseProductGroup.objects.published_by_mentor(user=mentor.user)
        return context

