# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from vanilla import TemplateView

from apps_data.courseevent.models.courseevent import CourseEventParticipation

from ..mixins.base import CourseMenuMixin


class CourseParticipantListView(CourseMenuMixin, TemplateView):
    """
    Owners of the course are listed
    """
    template_name = 'coursebackend/participant/list.html'

    def get_context_data(self, **kwargs):
        context = super(CourseParticipantListView, self).get_context_data(**kwargs)

        context['participants'] = context['courseevent'].students()

        return context

