# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.forms.models import modelform_factory

from django.views.generic import DetailView, TemplateView, FormView
from django.shortcuts import get_object_or_404

from apps_data.courseevent.models.courseevent import CourseEvent
from mentoki_products.models.courseeventproduct import CourseEventProduct
from apps_data.course.models.course import CourseOwner


class CourseEventListView(TemplateView):
    template_name = "courseoffer/pages/courselist.html"

    def get_context_data(self, **kwargs):
        """
        Events that are open for booking are shown. Also previews are shown as coming soon
        """
        context = super(CourseEventListView, self).get_context_data()

        # build list of course events
        context['courseevents'] = CourseEventProduct.objects.all().select_related('courseevent')
        print context
        return context


class CourseEventProductView(TemplateView):
    """
    This View shows the details of a courseevents. From here you can book them, if they are
    available for booking yet.
    """
    template_name = "courseoffer/pages/detail.html"

    def get_context_data(self, **kwargs):
        context = super(CourseEventProductView, self).get_context_data()
        courseevent = get_object_or_404(CourseEvent,slug=self.kwargs['slug'])
        context['teachersinfo'] = CourseOwner.objects.teachers_courseinfo_display(
            course=courseevent.course)
        context['courseevent'] = courseevent
        context['courseeventproduct'] = courseevent.courseeventproduct
        print context

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