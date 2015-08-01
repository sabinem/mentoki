# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404

from apps_data.courseevent.models.courseevent import CourseEvent

from ..mixins.base import CourseMenuMixin

class CourseEventMixin(CourseMenuMixin):

    def get_context_data(self, **kwargs):
        context = super(CourseEventMixin, self).get_context_data(**kwargs)

        courseevent = get_object_or_404(CourseEvent, slug=self.kwargs['slug'])

        context['courseevent'] = courseevent

        return context