# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.views.generic import TemplateView

from braces.views import LoginRequiredMixin

from apps_data.courseevent.models.courseevent import CourseEvent, CourseEventParticipation
from apps_data.course.models.course import Course, CourseOwner


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

