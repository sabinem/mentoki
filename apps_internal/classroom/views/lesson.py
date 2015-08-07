# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.shortcuts import get_object_or_404

from vanilla import TemplateView

from apps_data.course.models.lesson import Lesson

from .mixins.base import ClassroomMenuMixin


class LessonStartView(ClassroomMenuMixin, TemplateView):
    """
    Shows one lesson-step
    """
    def get_context_data(self, **kwargs):
        context = super(LessonStartView, self).get_context_data(**kwargs)

        context['nodes'] = \
            Lesson.objects.lessons_published_in_courseevent(courseevent=context['courseevent'])

        return context


class LessonBlockDetailView(ClassroomMenuMixin, TemplateView):
    """
    List all lesson-steps of a lesson
    """
    def get_context_data(self, **kwargs):
        context = super(LessonBlockDetailView, self).get_context_data(**kwargs)

        lessonblock = get_object_or_404(Lesson, pk=self.kwargs['pk'])

        context['lessonblock'] = lessonblock
        context['lessons'] = lessonblock.get_published_children(courseevent=context['courseevent'])

        return context


class LessonDetailView(ClassroomMenuMixin, TemplateView):
    """
    List all lesson-steps of a lesson
    """
    def get_context_data(self, **kwargs):
        context = super(LessonDetailView, self).get_context_data(**kwargs)

        lesson = get_object_or_404(Lesson, pk=self.kwargs['pk'])

        context['lesson'] = lesson
        context['breadcrumbs'] = lesson.get_ancestors()
        context['next_lesson'] = lesson.get_next_published_sibling(courseevent=context['courseevent'])
        context['previous_lesson'] = lesson.get_previous_published_sibling(courseevent=context['courseevent'])
        context['nodes'] = lesson.get_tree_with_material
        context['lessonsteps'] = lesson.get_children()

        return context


class LessonStepDetailView(ClassroomMenuMixin, TemplateView):
    """
    Shows one lesson-step
    """
    def get_context_data(self, **kwargs):
        context = super(LessonStepDetailView, self).get_context_data(**kwargs)

        lessonstep = get_object_or_404(Lesson, pk=self.kwargs['pk'])

        context['lessonstep'] = lessonstep
        context['breadcrumbs'] = lessonstep.get_ancestors()
        context['next_lessonstep'] = lessonstep.get_next_sibling()
        context['previous_lessonstep'] = lessonstep.get_previous_sibling()
        #context['materials'] = lessonstep.get_material

        return context