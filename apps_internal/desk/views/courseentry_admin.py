# coding: utf-8

"""
Entrypoint for updtaing and viewing the users profile
"""
#TODO: update possiblity is missing so far

from __future__ import unicode_literals, absolute_import

from django.views.generic import TemplateView
from django.core.exceptions import ObjectDoesNotExist

from braces.views import SuperuserRequiredMixin

from apps_data.course.models.course import Course
from apps_data.courseevent.models.courseevent import CourseEvent

import logging
logger = logging.getLogger('activity.users')


class CourseEntryAdminView(
    SuperuserRequiredMixin,
    TemplateView):
    """
    This view shows the users profile with his different roles
    as mentor and as customer
    """
    template_name = 'desk/pages/courseentry_admin.html'

    def get_context_data(self, **kwargs):
        """
        gets the users profile as mentor and customer
        """
        context = super(CourseEntryAdminView, self).get_context_data(**kwargs)
        context['courses'] = Course.objects.all()
        context['courseevents_active'] = CourseEvent.objects.active_closed_courseevents()
        context['courseevents_open'] = CourseEvent.objects.active_open_courseevents()

        return context


