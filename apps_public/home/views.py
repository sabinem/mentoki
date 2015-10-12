# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.views.generic import TemplateView, RedirectView, DetailView
from django.shortcuts import get_object_or_404

from userprofiles.models.mentor import MentorsProfile
from apps_data.course.models.course import CourseOwner
from apps_pagedata.textchunks.models import PublicTextChunks
from accounts.models import User


class HomePageView(TemplateView):
    template_name = "home/pages/homepage.html"


class CourseAGBPageView(TemplateView):
    template_name = "home/pages/motivation.html"


class StandardPageView(DetailView):
    template_name = "home/pages/textpage.html"
    context_object_name = 'textchunk'

    def get_object(self, queryset=None):
        """
        Returns the object the view is displaying.
        By default this requires `self.queryset` and a `pk` or `slug` argument
        in the URLconf, but subclasses can override this to return any object.
        """
        pagecode = self.kwargs['pagecode']
        textchunk = get_object_or_404(PublicTextChunks, pagecode=pagecode)
        return textchunk



class MotivationPageView(TemplateView):
    template_name = "home/pages/motivation.html"


class AboutPageView(TemplateView):
    template_name = "home/pages/about.html"

    def get_context_data(self, **kwargs):
        context = super(AboutPageView, self).get_context_data()

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
        context['courseevents'] = mentor.teaching_preview()
        print context
        return context