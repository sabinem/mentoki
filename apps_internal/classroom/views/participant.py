# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.views.generic import TemplateView

from apps_data.courseevent.models.courseevent import CourseEventParticipation

from .mixins.base import ClassroomMenuMixin

import logging
logger = logging.getLogger('display.classroom')

class CourseParticipantListView(ClassroomMenuMixin, TemplateView):
    """
    lists participants of the courseevent
    """
    def get_context_data(self, **kwargs):
        context = super(CourseParticipantListView, self).get_context_data(**kwargs)

        context['participants'] = CourseEventParticipation.objects.active_learners(
            courseevent=context['courseevent'])
        logger.info('Teilnehmerliste im Kurs %s: Anzahl %s' %
                    (context['courseevent'].slug, context['participants'].count()))

        return context
