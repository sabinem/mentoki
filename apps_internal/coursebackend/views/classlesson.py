# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.core.urlresolvers import reverse_lazy

from django.views.generic import DetailView, TemplateView, UpdateView, DeleteView, FormView

from braces.views import FormValidMessageMixin

from ..forms.classlesson import ClassLessonForm, ClassLessonStepForm
from ..forms.lessoncopy import LessonCopyForm

from apps_data.lesson.models.classlesson import ClassLesson
from apps_data.lesson.models.lesson import Lesson

from apps_data.lesson.utils.lessoncopy import copy_lesson_selected


from .mixins.base import CourseMenuMixin


class CopyLessonListView(CourseMenuMixin, TemplateView):
    """
    List all lesson blocks with lessons underneath
    """
    def get_context_data(self, **kwargs):
        context = super(CopyLessonListView, self).get_context_data(**kwargs)

        context['copied_lesson_ids'] = \
            ClassLesson.objects.copied_lesson_ids(courseevent=context['courseevent'])
        context['lessons'] = \
            Lesson.objects.lessons_for_course(course=context['course'])
        print context
        return context


class LessonStartView(CourseMenuMixin, TemplateView):
    """
    List all lesson blocks with lessons underneath
    """
    def get_context_data(self, **kwargs):
        context = super(LessonStartView, self).get_context_data(**kwargs)

        context['nodes'] = \
            ClassLesson.objects.complete_tree_for_courseevent(courseevent=context['courseevent'])

        return context


class BlockDetailView(CourseMenuMixin, DetailView):
    """
    List all lesson blocks with lessons underneath
    """
    model = ClassLesson
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
    model = ClassLesson
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
    model = ClassLesson
    context_object_name ='lessonstep'

    def get_context_data(self, **kwargs):
        context = super(StepDetailView, self).get_context_data(**kwargs)

        lessonstep = context['lessonstep']

        context['next_node'] = lessonstep.get_next_sibling()
        context['previous_node'] = lessonstep.get_previous_sibling()
        context['breadcrumbs'] = lessonstep.get_ancestors(include_self=True)

        return context


class LessonSuccessUrlMixin(object):

    def get_success_url(self):
       """
       for create update and delete view
       """
       return reverse_lazy('coursebackend:lesson_courseevent:start',
                           kwargs={'course_slug': self.kwargs['course_slug'],
                                   'slug': self.kwargs['slug']})

class LessonBreadcrumbMixin(object):

    def get_context_data(self, **kwargs):
        context = super(LessonBreadcrumbMixin, self).get_context_data(**kwargs)
        if 'object' in context:
            context['breadcrumbs'] = context['object'].get_ancestors(include_self=True)
        return context


class LessonUpdateView(CourseMenuMixin, FormValidMessageMixin, LessonSuccessUrlMixin, UpdateView):
    form_class = ClassLessonForm
    model = ClassLesson
    context_object_name ='lesson'
    form_valid_message = "Die Lektion wurde geändert!"

    def get_form_kwargs(self):
        course_slug = self.kwargs['course_slug']
        kwargs = super(LessonUpdateView, self).get_form_kwargs()
        kwargs['course_slug']=course_slug
        return kwargs


class LessonStepUpdateView(CourseMenuMixin, FormValidMessageMixin, LessonSuccessUrlMixin, UpdateView):
    form_class = ClassLessonStepForm
    model = ClassLesson
    context_object_name ='lessonstep'
    form_valid_message = "Der Lernabschnitt wurde geändert!"

    def get_form_kwargs(self):
        course_slug = self.kwargs['course_slug']
        kwargs = super(LessonStepUpdateView, self).get_form_kwargs()
        kwargs['course_slug']=course_slug
        return kwargs


class LessonDeleteView(CourseMenuMixin, FormValidMessageMixin, LessonSuccessUrlMixin, DeleteView):
    model=ClassLesson
    context_object_name = 'lesson'
    form_valid_message = "Der Lektionsbaum wurde gelöscht!"

    def get_context_data(self, **kwargs):
        context = super(LessonDeleteView, self).get_context_data(**kwargs)
        context['nodes'] = context['object'].get_descendants(include_self=True)
        return context


class CopyLessonView(CourseMenuMixin, FormValidMessageMixin, FormView):
    """
    List all lesson blocks with lessons underneath
    """
    form_class = LessonCopyForm
    form_valid_message = "Die Lektion wurde wie gewünscht kopiert!"

    def get_form_kwargs(self):
        lesson_pk = self.kwargs['pk']
        kwargs = super(CopyLessonView, self).get_form_kwargs()
        kwargs['lesson_pk']=lesson_pk
        return kwargs

    def get_success_url(self):
       """
       for create update and delete view
       """
       return reverse_lazy('coursebackend:lesson_courseevent:start',
                           kwargs={'course_slug': self.kwargs['course_slug'],
                                   'slug': self.kwargs['slug']})

    def form_valid(self, form):
        copied = copy_lesson_selected(self,
            lesson=form.lesson,
            lessonsteps=form.cleaned_data['copy_lessonsteps'],
            copy_lesson=form.cleaned_data['copy_lesson']
        )

        return super(CopyLessonView, self).form_valid(form)