# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse_lazy

from vanilla import UpdateView, DeleteView, CreateView, DetailView, TemplateView
from django.views.generic import DetailView, TemplateView, UpdateView, DeleteView, CreateView

from mptt.forms import TreeNodeChoiceField

from braces.views import MessageMixin

from .mixins.lesson import CourseFormMixin
from ..forms.lesson import LessonBlockForm, LessonForm, LessonStepForm
from ..forms.lessonold import LessonUpdateForm, LessonAddMaterialForm, LessonMoveForm, LessonCreateForm

from apps_data.course.models.lesson import Lesson

from .mixins.base import CourseMenuMixin


class LessonStartView(CourseMenuMixin, TemplateView):
    """
    List all lesson blocks with lessons underneath
    """
    def get_context_data(self, **kwargs):
        context = super(LessonStartView, self).get_context_data(**kwargs)

        context['nodes'] = Lesson.objects.complete_tree_for_course(course=context['course'])

        return context


class BlockDetailView(CourseMenuMixin, DetailView):
    """
    List all lesson blocks with lessons underneath
    """
    model = Lesson
    context_object_name ='lessonblock'

    def get_context_data(self, **kwargs):
        context = super(BlockDetailView, self).get_context_data(**kwargs)

        lessonblock = context['lessonblock']

        context['next_node'] = lessonblock.get_next_sibling()
        context['previous_node'] = lessonblock.get_previous_sibling()
        context['breadcrumbs'] = lessonblock.get_ancestors(include_self=True)

        context['nodes'] = lessonblock.get_tree_without_material
        return context


class LessonDetailView(CourseMenuMixin, DetailView):
    """
    List all lesson blocks with lessons underneath
    """
    model = Lesson
    context_object_name ='lesson'

    def get_context_data(self, **kwargs):
        context = super(LessonDetailView, self).get_context_data(**kwargs)

        lesson = context['lesson']

        context['next_node'] = lesson.get_next_sibling()
        context['previous_node'] = lesson.get_previous_sibling()
        context['breadcrumbs'] = lesson.get_ancestors(include_self=True)

        context['nodes'] = lesson.get_tree_with_material
        return context


class StepDetailView(CourseMenuMixin, DetailView):
    """
    List all lesson blocks with lessons underneath
    """
    model = Lesson
    context_object_name ='lessonstep'

    def get_context_data(self, **kwargs):
        context = super(StepDetailView, self).get_context_data(**kwargs)

        lessonstep = context['lessonstep']

        context['next_node'] = lessonstep.get_next_sibling()
        context['previous_node'] = lessonstep.get_previous_sibling()
        context['breadcrumbs'] = lessonstep.get_ancestors(include_self=True)

        return context


class LessonWorkView(CourseMenuMixin, TemplateView):
    """
    List all lesson blocks with lessons underneath
    """
    def get_context_data(self, **kwargs):
        context = super(LessonWorkView, self).get_context_data(**kwargs)

        context['nodes'] = Lesson.objects.complete_tree_for_course(course=context['course'])

        return context


class LessonMixin(CourseMenuMixin, MessageMixin):

    def get_success_url(self):
       """
       for create update and delete view
       """
       self.messages.info(self.success_msg)
       return reverse_lazy('coursebackend:lesson:work',
                           kwargs={'course_slug': self.kwargs['course_slug']})

    def get_context_data(self, **kwargs):
        context = super(LessonMixin, self).get_context_data(**kwargs)
        context['breadcrumbs'] = context['object'].get_ancestors(include_self=True)
        return context



class BlockUpdateView(LessonMixin, UpdateView):
    form_class = LessonBlockForm
    model = Lesson
    context_object_name ='lessonblock'
    success_msg = "Der Block wurde geändert!"


class LessonUpdateView(LessonMixin, UpdateView):
    form_class = LessonForm
    model = Lesson
    context_object_name ='lesson'
    success_msg = "Die Lektion wurde geändert!"

    def get_form_kwargs(self):
        course_slug = self.kwargs['course_slug']
        kwargs = super(LessonUpdateView, self).get_form_kwargs()
        kwargs['course_slug']=course_slug
        return kwargs


class LessonStepUpdateView(LessonMixin, UpdateView):
    form_class = LessonStepForm
    model = Lesson
    context_object_name ='lessonstep'
    success_msg = "Der Lernabschnitt wurde geändert!"

    def get_form_kwargs(self):
        course_slug = self.kwargs['course_slug']
        kwargs = super(LessonStepUpdateView, self).get_form_kwargs()
        kwargs['course_slug']=course_slug
        return kwargs


class LessonDeleteView(LessonMixin, DeleteView):
    model=Lesson
    context_object_name = 'lesson'
    success_msg = "Der Lektionsbaum wurde gelöscht!"

    def get_context_data(self, **kwargs):
        context = super(LessonDeleteView, self).get_context_data(**kwargs)
        context['nodes'] = context['object'].get_descendants(include_self=True)
        return context


class BlockCreateView(LessonMixin, UpdateView):
    form_class = LessonBlockForm
    model = Lesson
    context_object_name ='lessonblock'
    success_msg = "Der Block wurde angelegt!"


class LessonCreateView(LessonMixin, UpdateView):
    form_class = LessonForm
    model = Lesson
    context_object_name ='lesson'
    success_msg = "Die Lektion wurde angelegt!"

    def get_form_kwargs(self):
        course_slug = self.kwargs['course_slug']
        kwargs = super(LessonCreateView, self).get_form_kwargs()
        kwargs['course_slug']=course_slug
        return kwargs


class LessonStepCreateView(LessonMixin, UpdateView):
    form_class = LessonStepForm
    model = Lesson
    context_object_name ='lessonstep'
    success_msg = "Der Lernabschnitt wurde angelegt!"

    def get_form_kwargs(self):
        course_slug = self.kwargs['course_slug']
        kwargs = super(LessonStepCreateView, self).get_form_kwargs()
        kwargs['course_slug']=course_slug
        return kwargs

