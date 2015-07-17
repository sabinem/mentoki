# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.views.generic import TemplateView

from braces.views import LoginRequiredMixin

from apps_data.courseevent.models import CourseEvent, CourseEventParticipation
from apps_data.course.models import Course, CourseOwner


class DeskStartView(LoginRequiredMixin, TemplateView):
    """
    This View is the desk. It is the main entry point for every authenticated user.
    """
    template_name = 'desk/start.html'

    def get_context_data(self, **kwargs):

        context = super(DeskStartView, self).get_context_data(**kwargs)
        current_user = self.request.user

        if current_user.is_superuser:

            context['teach_courses'] = Course.objects.all()
            context['study_courseevents'] = CourseEvent.objects.all()

        else:

            context['study_courseevents'] = Course.objects.studying(user=self.request.user)
            study_courseevent_ids = \
                CourseEventParticipation.objects.filter(user=self.request.user).\
                values_list('courseevent_id', flat=True)

            # getting courseevents and corresponding courses
            courseevents = CourseEvent.objects.select_related('course').\
                filter(id__in=study_courseevent_ids).order_by('start_date')
            context['study_courseevents'] = courseevents

            # getting the ids of the courses that the user teaches
            teach_course_ids = CourseOwner.objects.filter(user=self.request.user.id).\
                values_list('course_id', flat=True)

            #getting the courses
            courses = Course.objects.filter(id__in=teach_course_ids)
            context['teach_courses'] = courses

            if current_user.is_staff:
                context['user_is_editor'] = True
            else:
                context['user_is_editor'] = False
        return context


class DeskTestView(LoginRequiredMixin, TemplateView):
    """
    This View is the desk. It is the main entry point for every authenticated user.
    """
    template_name = 'desk/test.html'
