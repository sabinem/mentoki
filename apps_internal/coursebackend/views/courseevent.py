# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.forms.models import modelform_factory
from django.core.urlresolvers import reverse_lazy
from django.forms.models import model_to_dict
from django.forms.widgets import NumberInput, DateInput,TextInput, Select
from django.views.generic import DetailView, UpdateView, TemplateView

from braces.views import FormValidMessageMixin

from froala_editor.widgets import FroalaEditor

from apps_data.courseevent.models.courseevent import CourseEvent

from .mixins.base import CourseMenuMixin


class CourseEventDetailView(CourseMenuMixin, DetailView):
    """
    Start in this section of the website: it shows the course and its attributes
    """
    model = CourseEvent
    slug_url_kwarg = 'slug'
    slug_field = 'slug'
    context_object_name ='courseevent'


class CourseEventListView(CourseMenuMixin, TemplateView):
    """
    Start in this section of the website: it shows the course and its attributes
    """
    def get_context_data(self, **kwargs):
        context = super(CourseEventListView, self).get_context_data(**kwargs)

        context['courseevents'] = CourseEvent.objects.active_courseevents_for_course(course=context['course'])

        return context


class CourseEventUpdateView(CourseMenuMixin, FormValidMessageMixin, UpdateView):
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
        elif field_name in ['video_url', 'title']:
            widget = TextInput
        elif field_name == 'start_date':
            widget = DateInput
        elif field_name in ['status_internal', 'event_type']:
            widget = Select
        elif field_name in ['target_group',
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

    def get_context_data(self, **kwargs):
        context = super(CourseEventUpdateView, self).get_context_data(**kwargs)

        course_dict = model_to_dict(context['course'])
        if self.kwargs['field'] in course_dict:
            context['exampletext'] = course_dict[self.kwargs['field']]

        return context
