# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.views.generic import TemplateView, UpdateView, DeleteView, CreateView
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404

from apps_data.course.models import Lesson, Course, Material

from ..mixins import CourseMenuMixin, CourseFormMixin, LessonMixin
from ..forms import LessonUpdateForm, LessonAddMaterialForm, LessonMoveForm, LessonCreateForm


class StartView(CourseMenuMixin, TemplateView):
    template_name = 'coursebackend/lessons_view/lesson_start.html'

    def get_context_data(self, **kwargs):
        context = super(StartView, self).get_context_data(**kwargs)

        context['nodes'] = Lesson.objects.filter(course=context['course'], level=0).\
            get_descendants(include_self=True)

        return context


class LessonBlockView(LessonMixin, TemplateView):
    template_name = 'coursebackend/lessons_view/detail_lesson_block.html'


class LessonDetailView(LessonMixin, TemplateView):
    template_name = 'coursebackend/lessons_view/detail_lesson_block.html'


class StepDetailView(LessonMixin, TemplateView):
    template_name = 'coursebackend/lessons_view/lesson_step.html'


class LessonUpdateView(CourseFormMixin, UpdateView):
    template_name = 'coursebackend/lesson_update/update.html'
    context_object_name = 'lesson'
    form_class = LessonUpdateForm

    def get_object(self, **kwargs):
        return get_object_or_404(Lesson, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super(LessonUpdateView, self).get_context_data(**kwargs)
        print "_________________"
        print "hallo"

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