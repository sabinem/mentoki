# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import get_object_or_404
from django.forms.models import modelform_factory
from django.forms.models import model_to_dict

from vanilla import UpdateView, DetailView

from apps_data.courseevent.models.courseevent import CourseEvent

from ..mixins.base import CourseMenuMixin


class CourseEventDetailView(CourseMenuMixin, DetailView):
    """
    Start in this section of the website: it shows the course and its attributes
    """
    model = CourseEvent
    template_name = 'coursebackend/courseevent/detail.html'
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'
    context_object_name ='courseevent'


class CourseEventUpdateView(CourseMenuMixin, UpdateView):
    """
    Update the course one field at a time
    """
    model = CourseEvent
    template_name = 'coursebackend/courseevent/update.html'
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'
    context_object_name ='courseevent'

    def get_form_class(self, **kwargs):
        return modelform_factory(CourseEvent, fields=(self.kwargs['field'],))

    def get_context_data(self, **kwargs):
        context = super(CourseEventUpdateView, self).get_context_data(**kwargs)

        course_dict = model_to_dict(context['course'])
        if self.kwargs['field'] in course_dict:
            context['exampletext'] = course_dict[self.kwargs['field']]

        return context
