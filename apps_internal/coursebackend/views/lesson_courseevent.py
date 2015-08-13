# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse_lazy

from django.views.generic import DetailView, TemplateView, UpdateView, DeleteView, FormView

from braces.views import FormValidMessageMixin

from ..forms.lesson import LessonBlockForm, LessonForm, LessonStepForm

from apps_data.lesson.models.classlesson import ClassLesson
from apps_data.lesson.models.lesson import Lesson
from apps_data.course.models.course import Course
from apps_data.lesson.utils import copy_lesson_for_courseevent
from apps_data.courseevent.models.courseevent import CourseEvent

from .mixins.base import CourseMenuMixin


class CopyLessonView(CourseMenuMixin, TemplateView):
    """
    List all lesson blocks with lessons underneath
    """
    def get_context_data(self, **kwargs):
        context = super(CopyLessonView, self).get_context_data(**kwargs)

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

        context['nodes'] = ClassLesson.objects.complete_tree_for_courseevent(courseevent=context['courseevent'])
        context['blocks_uncopied'] = Lesson.objects.blocks_uncopied(courseevent=context['courseevent'])

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


class LessonWorkView(CourseMenuMixin, TemplateView):
    """
    List all lesson blocks with lessons underneath
    """
    def get_context_data(self, **kwargs):
        context = super(LessonWorkView, self).get_context_data(**kwargs)

        context['nodes'] = ClassLesson.objects.complete_tree_for_courseevent(courseevent=context['courseevent'])

        return context


class LessonMixin(CourseMenuMixin, FormValidMessageMixin):

    def get_success_url(self):
       """
       for create update and delete view
       """
       return reverse_lazy('coursebackend:lesson_courseevent:work',
                           kwargs={'course_slug': self.kwargs['course_slug'],
                                   'slug': self.kwargs['slug']})

    def get_context_data(self, **kwargs):
        context = super(LessonMixin, self).get_context_data(**kwargs)
        if 'object' in context:
            context['breadcrumbs'] = context['object'].get_ancestors(include_self=True)
        return context



class BlockUpdateView(LessonMixin, UpdateView):
    form_class = LessonBlockForm
    model = ClassLesson
    context_object_name ='lessonblock'
    form_valid_message = "Der Block wurde geändert!"


class LessonUpdateView(LessonMixin, UpdateView):
    form_class = LessonForm
    model = ClassLesson
    context_object_name ='lesson'
    form_valid_message = "Die Lektion wurde geändert!"

    def get_form_kwargs(self):
        course_slug = self.kwargs['course_slug']
        kwargs = super(LessonUpdateView, self).get_form_kwargs()
        kwargs['course_slug']=course_slug
        return kwargs


class LessonStepUpdateView(LessonMixin, UpdateView):
    form_class = LessonStepForm
    model = ClassLesson
    context_object_name ='lessonstep'
    form_valid_message = "Der Lernabschnitt wurde geändert!"

    def get_form_kwargs(self):
        course_slug = self.kwargs['course_slug']
        kwargs = super(LessonStepUpdateView, self).get_form_kwargs()
        kwargs['course_slug']=course_slug
        return kwargs


class LessonDeleteView(LessonMixin, DeleteView):
    model=ClassLesson
    context_object_name = 'lesson'
    form_valid_message = "Der Lektionsbaum wurde gelöscht!"

    def get_context_data(self, **kwargs):
        context = super(LessonDeleteView, self).get_context_data(**kwargs)
        context['nodes'] = context['object'].get_descendants(include_self=True)
        return context


class BlockCreateView(LessonMixin, FormView):
    form_class = LessonBlockForm
    model = ClassLesson
    context_object_name ='lessonblock'
    form_valid_message = "Der Block wurde angelegt!"

    def form_valid(self, form):
        course = get_object_or_404(Course, slug=self.kwargs['course_slug'])
        lesson = Lesson.objects.create(
            course=course,
            title=form.cleaned_data['title'],
            description=form.cleaned_data['description'],
            text=form.cleaned_data['text']
        )
        return super(BlockCreateView, self).form_valid(form)


class LessonCreateView(LessonMixin, FormView):
    form_class = LessonForm
    model = ClassLesson
    context_object_name ='lesson'
    form_valid_message = "Die Lektion wurde angelegt!"

    def get_form_kwargs(self):
        course_slug = self.kwargs['course_slug']
        kwargs = super(LessonCreateView, self).get_form_kwargs()
        kwargs['course_slug']=course_slug
        return kwargs

    def form_valid(self, form):
        course = get_object_or_404(Course, slug=self.kwargs['course_slug'])
        lesson = Lesson.objects.create(
            course=course,
            title=form.cleaned_data['title'],
            description=form.cleaned_data['description'],
            text=form.cleaned_data['text'],
            parent=form.cleaned_data['parent']
        )
        return super(LessonCreateView, self).form_valid(form)


class LessonStepCreateView(LessonMixin, FormView):
    form_class = LessonStepForm
    model = ClassLesson
    context_object_name ='lessonstep'
    form_valid_message = "Der Lernabschnitt wurde angelegt!"

    def get_form_kwargs(self):
        courseevent_slug = self.kwargs['slug']
        kwargs = super(LessonStepCreateView, self).get_form_kwargs()
        kwargs['courseevent_slug']=courseevent_slug
        return kwargs

    def form_valid(self, form):
        courseevent=get_object_or_404(CourseEvent, slug=self.kwargs['slug'])
        course = courseevent.course

        classlesson = ClassLesson.objects.create_step(
            course=course,
            courseevent=courseevent,
            title=form.cleaned_data['title'],
            description=form.cleaned_data['description'],
            text=form.cleaned_data['text'],
            materials=form.cleaned_data['materials'],
            nr=form.cleaned_data['nr'],
            parent=form.cleaned_data['parent']
        )
        return super(LessonStepCreateView, self).form_valid(form)