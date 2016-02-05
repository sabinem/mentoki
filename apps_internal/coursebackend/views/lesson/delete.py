# coding: utf-8

"""
Lesson Delete View
"""

from __future__ import unicode_literals, absolute_import

from django.core.urlresolvers import reverse_lazy
from django.views.generic import DeleteView

from braces.views import FormValidMessageMixin

from apps_data.lesson.models.lesson import Lesson

from .mixins import LessonContextMixin


class LessonDeleteView(
    LessonContextMixin,
    FormValidMessageMixin,
    DeleteView):
    """
    delete lesson
    """
    model=Lesson
    context_object_name = 'lesson'
    form_valid_message = "Der Lektionsbaum wurde gelöscht!"

    def get_context_data(self, **kwargs):
        context = super(LessonDeleteView, self).get_context_data(**kwargs)
        context['nodes'] = context['object'].get_delete_tree
        return context

    def get_success_url(self):
        return reverse_lazy('coursebackend:lesson:start',
                           kwargs={'course_slug': self.kwargs['course_slug'],})