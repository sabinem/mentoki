# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

from braces.views import LoginRequiredMixin

from allauth.account.models import EmailAddress

from apps_data.courseevent.models.courseevent import CourseEvent, CourseEventParticipation
from apps_data.course.models.course import Course, CourseOwner
from apps_accountdata.userprofiles.models.mentor import MentorsProfile
from apps_customerdata.customer.models import Customer



class DeskStartView(LoginRequiredMixin, TemplateView):
    """
    This View is the desk. It is the main entry point for every authenticated user.
    """
    template_name = 'desk/pages/start.html'

    def get_context_data(self, **kwargs):

        context = super(DeskStartView, self).get_context_data(**kwargs)
        current_user = self.request.user

        if current_user.is_superuser:

            context['teach_courses'] = Course.objects.all()
            context['study_courseevents'] = CourseEvent.objects.all()

        else:

            context['teach_courses'] = self.request.user.teaching()
            context['study_courseevents'] = self.request.user.studying()

        return context


class DeskLearnView(LoginRequiredMixin, TemplateView):
    """
    This View is the desk. It is the main entry point for every authenticated user.
    """
    template_name = 'desk/pages/learn.html'

    def get_context_data(self, **kwargs):

        context = super(DeskLearnView, self).get_context_data(**kwargs)
        context['study_courseevents'] = self.request.user.studying()
        print context

        return context


class DeskTeachView(LoginRequiredMixin, TemplateView):
    """
    This View is the desk. It is the main entry point for every authenticated user.
    """
    template_name = 'desk/pages/teach.html'

    def get_context_data(self, **kwargs):

        context = super(DeskTeachView, self).get_context_data(**kwargs)
        context['teach_courses'] = self.request.user.teaching()

        return context


class DeskProfileView(LoginRequiredMixin, TemplateView):
    """
    This View is the desk. It is the main entry point for every authenticated user.
    """
    template_name = 'desk/pages/profile.html'

    def get_context_data(self, **kwargs):

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


class DeskAdminView(LoginRequiredMixin, TemplateView):
    """
    This View is the desk. It is the main entry point for every authenticated user.
    """
    template_name = 'desk/pages/start.html'

    def get_context_data(self, **kwargs):

        context = super(DeskAdminView, self).get_context_data(**kwargs)
        current_user = self.request.user

        if current_user.is_superuser:

            context['teach_courses'] = Course.objects.all()
            context['study_courseevents'] = CourseEvent.objects.all()

        else:

            context['teach_courses'] = self.request.user.teaching()
            context['study_courseevents'] = self.request.user.studying()

        return context