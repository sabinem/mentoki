# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.forms.models import modelform_factory

from django.views.generic import DetailView, TemplateView, FormView
from django.shortcuts import get_object_or_404

from apps_data.courseevent.models.courseevent import CourseEvent
from apps_data.course.models.course import CourseOwner


class CourseEventListView(TemplateView):
    template_name = "courseoffer/pages/courselist.html"

    def get_context_data(self, **kwargs):
        """
        Events that are open for booking are shown. Also previews are shown as coming soon
        """
        context = super(CourseEventListView, self).get_context_data()

        # build list of course events
        context['courseevents_now'] = CourseEvent.public_ready_for_booking.all()
        context['courseevents_preview'] = CourseEvent.public_ready_for_preview.all()

        return context


class CourseEventDetailView(DetailView):
    """
    This View shows the details of a courseevents. From here you can book them, if they are
    available for booking yet.
    """
    template_name = "courseoffer/pages/courselist.html"
    model = CourseEvent
    context_object_name ='courseevent'
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        context = super(CourseEventDetailView, self).get_context_data()

        context['teachersinfo'] = CourseOwner.objects.teachers_courseinfo_display(course=context['courseevent'].course)

        return context


class ChristineView(TemplateView):
    """
    This View shows the details of a courseevents. From here you can book them, if they are
    available for booking yet.
    """
    template_name = "courseoffer/pages/christine.html"

    def get_context_data(self, **kwargs):
        context = super(ChristineView, self).get_context_data()
        courseevent = get_object_or_404(CourseEvent, pk=4)
        context['teachersinfo'] = CourseOwner.objects.teachers_courseinfo_display(
            course=courseevent.course)
        context['courseevent'] = courseevent
        print context
        return context