# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.forms.models import modelform_factory
from django.forms.widgets import TextInput

from froala_editor.widgets import FroalaEditor

from vanilla import UpdateView, DetailView

from apps_data.course.models.course import Course

from .mixins.base import CourseMenuMixin


class CourseDetailView(CourseMenuMixin, DetailView):
    """
    Start in this section of the website: it shows the course and its attributes
    """
    model = Course
    template_name = 'coursebackend/course/pages/detail.html'
    lookup_field = 'slug'
    lookup_url_kwarg = 'course_slug'
    context_object_name ='course'


class CourseUpdateView(CourseMenuMixin, UpdateView):
    """
    Update the course one field at a time
    """
    model = Course
    template_name = 'coursebackend/course/pages/update.html'
    lookup_field = 'slug'
    lookup_url_kwarg = 'course_slug'
    context_object_name ='course'

    def get_form_class(self, **kwargs):
        field_name = self.kwargs['field']
        if field_name == 'title':
            widget = TextInput
        else:
            widget = FroalaEditor
        return modelform_factory(Course, fields=(field_name,),
                                 widgets={ field_name: widget })
