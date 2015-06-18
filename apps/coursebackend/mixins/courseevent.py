# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404

from apps.courseevent.models import CourseEvent, CourseEventPubicInformation

from ..mixins import CourseMenuMixin

class CourseEventMixin(CourseMenuMixin):

    def get_context_data(self, **kwargs):
        context = super(CourseEventMixin, self).get_context_data(**kwargs)

        courseevent = get_object_or_404(CourseEvent, slug=self.kwargs['slug'])
        courseeventpublicinformation = get_object_or_404(CourseEventPubicInformation, courseevent=courseevent)

        context['courseevent'] = courseevent
        context['courseeventinfo'] = courseeventpublicinformation

        return context