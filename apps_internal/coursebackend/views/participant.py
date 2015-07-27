# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from vanilla import TemplateView

from apps_data.courseevent.models import CourseEventParticipation

from ..mixins import CourseMenuMixin


class CourseParticipantListView(CourseMenuMixin, TemplateView):
    """
    Owners of the course are listed
    """
    template_name = 'participant/participantslist.html'

    def get_context_data(self, **kwargs):
        context = super(CourseParticipantListView, self).get_context_data(**kwargs)

        courseevent = CourseEvent.objects.get(slug=kwargs['slug'])

        context['courseevent'] = courseevent
        # course owners are selected together with their user data
        participants = CourseEventParticipation.objects.select_related('user').filter(courseevent_id=courseevent.id)
        # the context are the owners informations
        context['participants'] = participants
        try:
            # get courseevent from slug
            courseevent = CourseEvent.objects.get(slug=kwargs['slug'])
            context['courseevent'] = courseevent
            # course owners are selected together with their user data
            participants = CourseEventParticipation.objects.select_related('user').filter(courseevent_id=courseevent.id)
            # the context are the owners informations
            context['participants'] = participants
        except:
            pass
        print context['participants']
        print context['courseevent']
        return context

from django.shortcuts import get_object_or_404
from django.forms.models import modelform_factory

from vanilla import UpdateView, DetailView

from apps_data.courseevent.models import CourseEvent

from ..mixins import CourseMenuMixin


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