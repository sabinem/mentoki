# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.views.generic import DetailView, UpdateView
from django.forms.models import modelform_factory
from django.shortcuts import get_object_or_404

from apps.courseevent.models import CourseEvent, CourseEventPubicInformation
from ..mixins import CourseEventMixin


class CourseEventDetailView(CourseEventMixin, DetailView):
    model = CourseEvent
    context_object_name = 'courseevent'
    template_name = 'coursebackend/courseevent/detail.html'

    def get_context_data(self, **kwargs):
        context = super(CourseEventDetailView, self).get_context_data(**kwargs)

        courseeventpublicinformation = get_object_or_404(CourseEventPubicInformation, courseevent=context['courseevent'])

        context['courseeventinfo'] = courseeventpublicinformation

        return context


class CourseEventUpdateView(CourseEventMixin, UpdateView):
    model = CourseEvent
    template_name = 'coursebackend/courseevent/update.html'
    context_object_name = 'courseevent'

    def get_form_class(self, **kwargs):
        return modelform_factory(CourseEvent, fields=('status_internal',
                                                      'nr_weeks', 'max_participants', 'start_date',
                                                      'event_type'))


class CourseEventExcerptUpdateView(CourseEventMixin, UpdateView):
    model = CourseEvent
    template_name = 'coursebackend/courseevent/update.html'
    context_object_name = 'courseevent'

    def get_form_class(self, **kwargs):
        return modelform_factory(CourseEvent, fields=('excerpt',))

    def get_context_data(self, **kwargs):
        context = super(CourseEventUpdateView, self).get_context_data(**kwargs)

        context['exampletext'] = context['course'].excerpt

        return context


class CourseEventPublicInformationUpdateView(CourseEventMixin, UpdateView):
    model = CourseEventPubicInformation
    template_name = 'coursebackend/courseevent/update.html'
    context_object_name = 'courseevent'

    def get_form_class(self, **kwargs):
        return modelform_factory(CourseEventPubicInformation, fields=(self.kwargs['field'],))

    def get_context_data(self, **kwargs):
        context = super(CourseEventPublicInformationUpdateView, self).get_context_data(**kwargs)

        field = self.kwargs['field']
        if field == 'target_group':
            context['exampletext'] = context['course'].target_group
        elif field == 'prerequisites':
            context['exampletext'] = context['course'].prerequisites
        elif field == 'project':
            context['exampletext'] = context['course'].project
        elif field == 'structure':
            context['exampletext'] = context['course'].structure
        elif field == 'prerequisites':
            context['exampletext'] = context['course'].prerequisites
        elif field == 'text':
            context['exampletext'] = context['course'].text
        else:
            context['exampletext'] = 'Dieses Feld ist in der Kursvorlage nicht vorhanden.'
        return context
