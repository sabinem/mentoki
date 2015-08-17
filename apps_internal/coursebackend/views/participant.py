# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.views.generic import TemplateView

from .mixins.base import CourseMenuMixin


class CourseParticipantListView(
    CourseMenuMixin,
    TemplateView):
    """
    Participants of the course are listed
    """
    def get_context_data(self, **kwargs):
        context = super(CourseParticipantListView, self).get_context_data(**kwargs)

        context['participants'] = context['courseevent'].students()
        return context

