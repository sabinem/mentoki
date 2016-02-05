# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.views.generic import DeleteView
from django.core.urlresolvers import reverse_lazy

from braces.views import FormValidMessageMixin

from apps_data.lesson.models.classlesson import ClassLesson

from ..mixins.base import CourseMenuMixin, FormCourseEventKwargsMixin
from .mixin import ClassLessonBreadcrumbMixin, ClassLessonSuccessUpdateUrlMixin

import logging
logger = logging.getLogger(__name__)


class ClassLessonDeleteView(
    CourseMenuMixin,
    ClassLessonBreadcrumbMixin,
    FormValidMessageMixin,
    FormCourseEventKwargsMixin,
    ClassLessonSuccessUpdateUrlMixin,
    DeleteView):
    """
    Delete a classlesson
    """
    model = ClassLesson
    context_object_name = 'classlesson'
    form_valid_message = "Der Unterricht wurde gelöscht!"

    def get_context_data(self, **kwargs):
        context = super(ClassLessonDeleteView, self).get_context_data(**kwargs)
        context['nodes'] = context['object'].get_delete_tree
        return context

    def get_success_url(self):
        return reverse_lazy('coursebackend:classlesson:start',
                           kwargs={'course_slug': self.kwargs['course_slug'],
                                   'slug': self.kwargs['slug']})