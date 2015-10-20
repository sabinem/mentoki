# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.views.generic import TemplateView, RedirectView, DetailView
from django.shortcuts import get_object_or_404

from apps_accountdata.userprofiles.models.mentor import MentorsProfile
from apps_pagedata.textchunks.models import PublicTextChunks
from accounts.models import User
from apps_productdata.mentoki_product.models.courseproductgroup import CourseProductGroup

class PageTextMixin(object):
    context_object_name = 'textchunk'

    def get_object(self, queryset=None):
        """
        the pagechunk according to the pagecode
        """
        pagecode = self.kwargs['pagecode']
        textchunk = get_object_or_404(PublicTextChunks, pagecode=pagecode)
        return textchunk


class HomePageView(TemplateView):
    template_name = "home/pages/homepage.html"


class CourseAGBPageView(
    PageTextMixin,
    DetailView):
    template_name = "home/pages/courseagb.html"


class StandardPageView(
    PageTextMixin,
    DetailView):
    template_name = "home/pages/standards.html"


class TeachOnlinePageView(
    PageTextMixin,
    DetailView):
    template_name = "home/pages/unterrichten.html"


class CourseReadyPageView(
    PageTextMixin,
    DetailView):
    template_name = "home/pages/fertigen-kurs-anbieten.html"


class EducationMentoringPageView(
    PageTextMixin,
    DetailView):
    template_name = "home/pages/bildungsmentoring.html"


class MotivationPageView(TemplateView):
    template_name = "home/pages/motivation.html"


class AboutPageView(TemplateView):
    template_name = "home/pages/about.html"


class ImpressumPageView(
    PageTextMixin,
    DetailView):
    template_name = "home/pages/textpage.html"


class StarterkursPageView(
    PageTextMixin,
    DetailView):
    template_name = "home/pages/textpage.html"


class MentorsListView(TemplateView):
    template_name = "home/pages/mentors.html"

    def get_context_data(self, **kwargs):
        context = super(MentorsListView, self).get_context_data()

        # get mentor_profile
        mentors = MentorsProfile.objects.all().select_related('user').order_by('display_nr')
        context['mentors'] = mentors

        print context
        return context


class MentorsPageView(TemplateView):
    template_name = "home/pages/mentor.html"

    def get_context_data(self, **kwargs):
        context = super(MentorsPageView, self).get_context_data()

        # get user from username
        user = User.objects.get(username=self.kwargs['username'])

        # get mentor_profile
        mentor = get_object_or_404(MentorsProfile, user=user)
        context['mentor'] = mentor

        #get courses
        context['courseproductgroups'] = CourseProductGroup.objects.by_mentor(user=user)
        print context
        return context