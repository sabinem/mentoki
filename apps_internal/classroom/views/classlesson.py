# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from apps_data.lesson.models.classlesson import ClassLesson

from .mixins.base import ClassroomMenuMixin


class ClassLessonStartView(
    ClassroomMenuMixin,
    TemplateView):
    """
    Shows all classlessons that are published in the class (have a menu entry in the classroom menu)
    """
    def get_context_data(self, **kwargs):
        context = super(ClassLessonStartView, self).get_context_data(**kwargs)

        context['nodes'] = \
            ClassLesson.objects.lessons_for_courseevent(courseevent=context['courseevent'])

        return context


class ClassLessonBlockDetailView(
    ClassroomMenuMixin,
    TemplateView):
    """
    List all classlessons of a block that are published in the classroom
    """
    def get_context_data(self, **kwargs):
        context = super(ClassLessonBlockDetailView, self).get_context_data(**kwargs)

        lessonblock = get_object_or_404(ClassLesson, pk=self.kwargs['pk'])

        context['lessonblock'] = lessonblock
        context['lessons'] = lessonblock.get_published_children(courseevent=context['courseevent'])

        return context


class ClassLessonDetailView(
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
        context['breadcrumbs'] = lesson.get_ancestors()
        context['next_lesson'] = lesson.get_next_sibling()
        context['previous_lesson'] = lesson.get_previous_sibling()
        context['lessonsteps'] = lesson.get_children()

        return context


class ClassLessonStepDetailView(
    ClassroomMenuMixin,
    TemplateView):
    """
    Shows one classlesson-step
    """
    def get_context_data(self, **kwargs):
        context = super(ClassLessonStepDetailView, self).get_context_data(**kwargs)

        lessonstep = get_object_or_404(ClassLesson, pk=self.kwargs['pk'])

        context['lessonstep'] = lessonstep
        context['breadcrumbs'] = lessonstep.get_ancestors()
        context['next_lessonstep'] = lessonstep.get_next_sibling()
        context['previous_lessonstep'] = lessonstep.get_previous_sibling()
        return context