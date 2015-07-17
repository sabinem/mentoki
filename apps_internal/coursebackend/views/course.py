# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.views.generic import TemplateView, UpdateView, ListView
from django.forms.models import modelform_factory
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse

from apps_data.course.models import Course
from ..mixins import CourseMenuMixin, CourseEventMixin


class CourseDetailView(CourseMenuMixin, TemplateView):
    """
    Start in this section of the website: it shows the course and its attributes
    """
    template_name = 'coursebackend/course/detail.html'


class CourseUpdateView(CourseMenuMixin, UpdateView):
    """
    Here course owner can update the information on the course general description
    """
    model = Course
    template_name = 'coursebackend/course/update.html'

    def get_object(self, **kwargs):
        return get_object_or_404(Course, slug=self.kwargs['course_slug'])

    def get_form_class(self, **kwargs):
        return modelform_factory(Course, fields=(self.kwargs['field'],))

    def get_success_url(self):
        return reverse('coursebackend:course:detail', kwargs={"course_slug": self.kwargs['course_slug']})