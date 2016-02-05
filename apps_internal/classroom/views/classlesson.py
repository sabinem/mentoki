# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, FormView, DetailView

from apps_data.courseevent.models.menu import ClassroomMenuItem
from apps_data.lesson.models.classlesson import ClassLesson

from .mixins.base import ClassroomMenuMixin, AuthClassroomAccessMixin


class ClassLessonStartView(
    AuthClassroomAccessMixin,
    ClassroomMenuMixin,
    TemplateView):
    """
    Shows all classlessons that are published in the class (have a menu entry in the classroom menu)
    """
    def get_context_data(self, **kwargs):
        context = super(ClassLessonStartView, self).get_context_data(**kwargs)

        context['lesson_items'] = \
            ClassroomMenuItem.objects.lessons_for_courseevent(
                courseevent=context['courseevent'])

        return context


class ClassLessonDetailView(
    AuthClassroomAccessMixin,
    ClassroomMenuMixin,
    TemplateView):
    """
    Show classlesson in Detail
    List all classlesson-steps of a lesson (they are all published along with the lesson)
    """
    def get_context_data(self, **kwargs):
        context = super(ClassLessonDetailView, self).get_context_data(**kwargs)

        lesson = get_object_or_404(ClassLesson, pk=self.kwargs['pk'])

        context['lesson'] = lesson
        context['breadcrumbs'] = lesson.get_published_breadcrumbs_with_self
        context['next_node'] = lesson.get_next_sibling_published
        context['previous_node'] = lesson.get_previous_sibling_published
        context['lessonsteps'] = lesson.get_children()

        return context

