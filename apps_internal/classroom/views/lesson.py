# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.shortcuts import get_object_or_404

from vanilla import TemplateView

from apps_data.course.models.lesson import Lesson

from .mixins.lesson import ClassroomMenuMixin


class LessonMixin(ClassroomMenuMixin):

    def get_context_data(self, **kwargs):
        context = super(LessonMixin, self).get_context_data(**kwargs)

        start_node = get_object_or_404(Lesson, pk=self.kwargs['pk'])
        context['start_lesson'] = start_node
        context['next_node'] = start_node.get_next_sibling()
        context['previous_node'] = start_node.get_previous_sibling()
        context['breadcrumbs'] = start_node.get_ancestors()
        context['nodes'] = start_node.get_tree_with_material

        return context


class LessonStartView(ClassroomMenuMixin, TemplateView):
    """
    Shows one lesson-step
    """
    template_name = 'classroom/lesson/pages/start.html'

    def get_context_data(self, **kwargs):
        context = super(LessonStartView, self).get_context_data(**kwargs)

        context['nodes'] = \
            Lesson.objects.lessons_published_in_courseevent(courseevent=context['courseevent'])

        return context


class LessonDetailView(ClassroomMenuMixin, TemplateView):
    """
    List all lesson-steps of a lesson
    """
    template_name = 'classroom/lesson/pages/lesson.html'

    def get_context_data(self, **kwargs):
        context = super(LessonDetailView, self).get_context_data(**kwargs)

        lesson = get_object_or_404(Lesson, pk=self.kwargs['pk'])

        context['lesson'] = lesson
        context['breadcrumbs'] = lesson.get_ancestors()
        context['next_node'] = lesson.get_next_sibling()
        context['previous_node'] = lesson.get_previous_sibling()
        context['nodes'] = lesson.get_tree_with_material


        return context


class StepDetailView(ClassroomMenuMixin, TemplateView):
    """
    Shows one lesson-step
    """
    template_name = 'classroom/lesson/pages/lesson_step.html'

    def get_context_data(self, **kwargs):
        context = super(LessonDetailView, self).get_context_data(**kwargs)

        lesson = get_object_or_404(Lesson, pk=self.kwargs['pk'])

        context['lesson'] = lesson
        context['breadcrumbs'] = lesson.get_ancestors()
        context['next_node'] = lesson.get_next_sibling()
        context['previous_node'] = lesson.get_previous_sibling()
        context['nodes'] = lesson.get_tree_with_material

        return context