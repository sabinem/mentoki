# -*- coding: utf-8 -*-

"""
Views for internally viewing and editing courses. These views are only
accessible by teachers. Access is tested by CourseMenuMixin.


"""

from __future__ import unicode_literals

from django.forms.models import modelform_factory
from django.forms.widgets import TextInput
from django.views.generic import DetailView, UpdateView, TemplateView

from braces.views import FormValidMessageMixin

from froala_editor.widgets import FroalaEditor

from apps_data.course.models.course import Course
from apps_data.courseevent.models.courseevent import CourseEvent

from .mixins.base import CourseMenuMixin


class CourseDetailView(
    CourseMenuMixin,
    DetailView):
    """
    Start in this section of the website: it shows the course and its attributes
    """
    model = Course
    context_object_name ='course'
    slug_url_kwarg = 'course_slug'
    slug_field = 'slug'


class CourseUpdateView(
    CourseMenuMixin,
    FormValidMessageMixin,
    UpdateView):
    """
    Update the course one field at a time
    """
    model = Course
    slug_url_kwarg = 'course_slug'
    slug_field = 'slug'
    context_object_name ='course'
    form_valid_message="Die Kursvorlage wurde geändert!"

    def get_form_class(self, **kwargs):
        field_name = self.kwargs['field']
        if field_name == 'title':
            widget = TextInput
        else:
            widget = FroalaEditor
        return modelform_factory(Course, fields=(field_name,),
                                 widgets={ field_name: widget })


class CourseEventListView(
    CourseMenuMixin,
    TemplateView):
    """
    Start in this section of the website: it shows the course and its attributes
    """
    def get_context_data(self, **kwargs):
        context = super(CourseEventListView, self).get_context_data(**kwargs)

        context['courseevents'] = CourseEvent.objects.active_courseevents_for_course(course=context['course'])

        return context