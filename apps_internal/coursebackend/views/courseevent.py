# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.forms.models import modelform_factory
from django.forms.models import model_to_dict
from django.forms.widgets import NumberInput, DateInput,TextInput, Select, \
    CheckboxInput
from django.views.generic import DetailView, UpdateView, TemplateView
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from braces.views import FormValidMessageMixin

from froala_editor.widgets import FroalaEditor

from apps_data.courseevent.models.courseevent import CourseEvent
from apps_data.course.models.course import Course

from .mixins.base import CourseMenuMixin


class CourseEventDetailView(
    CourseMenuMixin,
    DetailView):
    """
    Start in this section of the website: it shows the course and its attributes
    """
    model = CourseEvent
    slug_url_kwarg = 'slug'
    slug_field = 'slug'
    context_object_name ='courseevent'


class CourseEventUpdateView(
    CourseMenuMixin,
    FormValidMessageMixin,
    UpdateView):
    """
    Update the course one field at a time
    """
    model = CourseEvent
    slug_url_kwarg = 'slug'
    slug_field = 'slug'
    context_object_name ='courseevent'
    form_valid_message="Das Kursereignis wurde geändert!"

    def get_form_class(self, **kwargs):
        field_name = self.kwargs['field']
        if field_name in ['max_participants', 'nr_weeks']:
            widget = NumberInput
        elif field_name in ['video_url', 'title', 'email_greeting']:
            widget = TextInput
        elif field_name in ['you_okay']:
            widget = CheckboxInput
        elif field_name == 'start_date':
            widget = DateInput
        elif field_name in ['status_internal', 'event_type']:
            widget = Select
        elif field_name in ['target_group',
                            'pricemodel',
                            'excerpt',
                            'text',
                            'format',
                            'workload',
                            'project',
                            'structure',
                            'project',
                            'prerequisites']:
            widget = FroalaEditor
        return modelform_factory(CourseEvent, fields=(field_name,),
                                 widgets={ field_name: widget })


class CopyCourseDescriptionView(
    CourseMenuMixin,
    TemplateView):
    """
    Update the course one field at a time
    """