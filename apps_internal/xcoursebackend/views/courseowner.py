# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.views.generic import UpdateView, TemplateView
from django.forms.models import modelform_factory
from django.core.urlresolvers import reverse

from apps_data.course.models import Course, CourseOwner
from ..mixins import CourseMenuMixin


class CourseOwnerListView(CourseMenuMixin, TemplateView):
    template_name = 'coursebackend/courseowner/list.html'

    def get_context_data(self, **kwargs):
        context = super(CourseOwnerListView, self).get_context_data(**kwargs)

        context['owners'] = CourseOwner.objects.teachers(course=context['course'])

        return context


class CourseOwnerUpdateView(CourseMenuMixin, UpdateView):
    model = CourseOwner
    template_name = 'coursebackend/courseowner/update.html'
    context_object_name = 'owner'
    form_class = modelform_factory(CourseOwner, fields=( 'text', 'display', 'display_nr', 'foto'))

    def get_success_url(self):
        return reverse('coursebackend:courseowner:list', kwargs={"course_slug": self.kwargs['course_slug'],})

    def get_object(self, queryset=None):
        return CourseOwner.objects.get(pk=self.kwargs['pk'])
