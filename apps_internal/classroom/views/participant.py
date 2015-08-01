# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from vanilla import TemplateView

from .mixins.base import ClassroomMenuMixin


class CourseParticipantListView(ClassroomMenuMixin, TemplateView):
    """
    Participants of the courseevent are listed
    """
    def get_context_data(self, **kwargs):
        context = super(CourseParticipantListView, self).get_context_data(**kwargs)

        context['participants'] = context['courseevent'].students()

        return context

