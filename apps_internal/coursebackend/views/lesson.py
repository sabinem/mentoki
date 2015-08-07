# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.views.generic import UpdateView, DeleteView, CreateView
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404

from .mixins.lesson import CourseFormMixin
from ..forms.lesson import LessonUpdateForm, LessonAddMaterialForm, LessonMoveForm, LessonCreateForm

from vanilla import UpdateView, DetailView, TemplateView

from apps_data.course.models.lesson import Lesson

from .mixins.base import CourseMenuMixin
from .mixins.lesson import LessonMixin


class LessonStartView(CourseMenuMixin, TemplateView):
    """
    List all lesson blocks with lessons underneath
    """
    def get_context_data(self, **kwargs):
        context = super(LessonStartView, self).get_context_data(**kwargs)

        context['nodes'] = Lesson.objects.complete_tree_for_course(course=context['course'])

        return context


class LessonBlockView(LessonMixin, TemplateView):
    """
    List all lesson blocks with lessons underneath
    """
    template_name = 'coursebackend/lessons_view/detail_lesson_block.html'


class LessonDetailView(LessonMixin, TemplateView):
    """
    List all lesson-steps of a lesson
    """
    template_name = 'coursebackend/lessons_view/detail_lesson_block.html'


class StepDetailView(LessonMixin, TemplateView):
    """
    Shows one lesson-step
    """
    template_name = 'coursebackend/lessons_view/lesson_step.html'


class LessonUpdateView(CourseFormMixin, UpdateView):
    template_name = 'coursebackend/lesson_update/update.html'
    context_object_name = 'lesson'
    form_class = LessonUpdateForm

    def get_object(self, **kwargs):
        return get_object_or_404(Lesson, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super(LessonUpdateView, self).get_context_data(**kwargs)

        context['breadcrumbs'] = context['lesson'].get_ancestors()

        return context


class LessonMoveView(CourseMenuMixin, UpdateView):
    template_name = 'coursebackend/lesson_update/move.html'
    context_object_name = 'lesson'
    form_class = LessonMoveForm

    def get_object(self, **kwargs):
        return get_object_or_404(Lesson, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super(LessonMoveView, self).get_context_data(**kwargs)

        context['breadcrumbs'] = context['lesson'].get_ancestors()

        context['nodes'] = context['lesson'].get_descendants(include_self=True).prefetch_related('material')

        return context


class LessonAddMaterialView(CourseFormMixin, UpdateView):
    template_name = 'coursebackend/lessons/update.html'
    context_object_name = 'lesson'
    form_class = LessonAddMaterialForm

    def get_object(self, **kwargs):
        return get_object_or_404(Lesson, pk=self.kwargs['pk'])


class LessonCreateView(CourseFormMixin, CreateView):
    template_name = 'coursebackend/lesson_update/create.html'
    form_class = LessonCreateForm


class LessonDeleteView(CourseMenuMixin, DeleteView):
    model=Lesson
    template_name = 'coursebackend/lesson_update/delete.html'
    context_object_name = 'lesson'

    def get_success_url(self):
        return reverse('coursebackend:lesson:start', kwargs={"course_slug": self.kwargs['course_slug'],})

    def get_context_data(self, **kwargs):
        context = super(LessonDeleteView, self).get_context_data(**kwargs)

        context['breadcrumbs'] = context['lesson'].get_ancestors()

        nodes = context['lesson'].get_descendants(include_self=True)
        context['nodes'] = nodes

        return context