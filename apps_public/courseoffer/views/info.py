# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.forms.models import modelform_factory

from django.views.generic import DetailView, TemplateView, FormView
from django.shortcuts import get_object_or_404

from apps_data.courseevent.models.courseevent import CourseEvent
from apps_customerdata.mentoki_product.models.courseevent import CourseEventProduct
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
        print "in courseevent list view"
        print context
        return context


class CourseEventProductMixin(object):

    def get_context_data(self, **kwargs):
        """
        gets product detail context
        """
        context = super(CourseEventProductMixin, self).get_context_data()
        courseevent = get_object_or_404(CourseEvent,slug=self.kwargs['slug'])
        context['slug'] = slug=self.kwargs['slug']
        context['teachersinfo'] = CourseOwner.objects.teachers_courseinfo_display(
            course=courseevent.course)
        context['courseevent'] = courseevent
        context['courseeventproduct'] = courseevent.courseeventproduct
        context['url_name'] = self.request.resolver_match.url_name
        print context

        return context


class CourseEventProductView(
    CourseEventProductMixin,
    TemplateView):
    """
    This View shows the details of a courseevents. From here you can book them, if they are
    available for booking yet.
    """
    template_name = "courseoffer/pages/detail.html"


class CourseEventMentorsView(
    CourseEventProductMixin,
    TemplateView):
    """
    This View shows the details of a courseevents. From here you can book them, if they are
    available for booking yet.
    """
    template_name = "courseoffer/pages/mentors.html"


class CourseEventAGBView(
    CourseEventProductMixin,
    TemplateView):
    """
    This View shows the details of a courseevents. From here you can book them, if they are
    available for booking yet.
    """
    template_name = "courseoffer/pages/agb.html"

