# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.views.generic import TemplateView, UpdateView, DeleteView, CreateView
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404

from apps.course.models import Lesson, Course, Material

from ..mixins import LessonsMenuMixin, CourseFormMixin
from ..forms import LessonForm, LessonAddMaterialForm


class StartView(LessonsMenuMixin, TemplateView):
    template_name = 'coursebackend/lessons/lesson_start.html'

    def get_context_data(self, **kwargs):
        context = super(StartView, self).get_context_data(**kwargs)

        context['nodes'] = Lesson.objects.filter(course=context['course'], level=0)

        return context


class LessonBlockView(LessonsMenuMixin, TemplateView):
    template_name = 'coursebackend/lessons/lesson_block.html'

    def get_context_data(self, **kwargs):
        context = super(LessonBlockView, self).get_context_data(**kwargs)

        start_node = Lesson.objects.get(pk=self.kwargs['pk'])

        context['start_node'] = start_node

        context['root_node'] = start_node.get_root()

        context['next_node'] = \
            start_node.get_next_sibling()

        context['previous_node'] = \
            start_node.get_previous_sibling()

        context['breadcrumbs'] = start_node.get_ancestors()

        context['nodes'] = start_node.get_descendants(include_self=True)

        return context


class LessonDetailView(LessonsMenuMixin, TemplateView):
    template_name = 'coursebackend/lessons/lesson_detail.html'

    def get_context_data(self, **kwargs):
        context = super(LessonsMenuMixin, self).get_context_data(**kwargs)


        start_node = Lesson.objects.get(pk=self.kwargs['pk'])

        context['start_node'] = start_node

        context['root_node'] = start_node.get_root()

        context['next_node'] = start_node.get_next_sibling()
        context['previous_node'] = start_node.get_previous_sibling()

        context['breadcrumbs'] = start_node.get_ancestors()
        context['nodes'] = start_node.get_descendants(include_self=True)

        return context


class StepDetailView(LessonsMenuMixin, TemplateView):
    template_name = 'coursebackend/lessons/lesson_step.html'

    def get_context_data(self, **kwargs):
        context = super(StepDetailView, self).get_context_data(**kwargs)

        context['nodes'] = Lesson.objects.filter(course=context['course'], level=0)

        return context


class LessonUpdateView(LessonsMenuMixin, CourseFormMixin, UpdateView):
    template_name = 'coursebackend/lessons/update.html'
    context_object_name = 'lesson'
    form_class = LessonForm

    def get_object(self, **kwargs):
        return get_object_or_404(Lesson, pk=self.kwargs['pk'])


class LessonAddMaterialView(LessonsMenuMixin, CourseFormMixin, UpdateView):
    template_name = 'coursebackend/lessons/update.html'
    context_object_name = 'lesson'
    form_class = LessonAddMaterialForm

    def get_object(self, **kwargs):
        return get_object_or_404(Lesson, pk=self.kwargs['pk'])


class LessonCreateView(LessonsMenuMixin, CourseFormMixin, CreateView):
    template_name = 'coursebackend/lessons/create.html'
    form_class = LessonForm


class LessonDeleteView(LessonsMenuMixin, DeleteView):
    model=Lesson
    template_name = 'coursebackend/lessons/delete.html'
    context_object_name = 'lesson'

    def get_success_url(self):
        return reverse('coursebackend:lesson:list', kwargs={"course_slug": self.kwargs['course_slug'],})

    def get_context_data(self, **kwargs):
        context = super(LessonDeleteView, self).get_context_data(**kwargs)

        nodes = context['lesson'].get_descendants(include_self=False)
        context['nodes'] = nodes

        return context