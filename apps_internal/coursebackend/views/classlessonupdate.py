# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import DetailView, TemplateView, UpdateView, \
    DeleteView, FormView
from django.core.validators import ValidationError

from braces.views import FormValidMessageMixin

from ..forms.classlesson import ClassLessonForm, ClassLessonStepForm,\
     ClassLessonBlockForm
from ..forms.lessoncopy import LessonCopyForm

from apps_data.lesson.models.classlesson import ClassLesson
from apps_data.lesson.models.lesson import Lesson
from apps_data.courseevent.models.courseevent import CourseEvent

from .mixins.base import CourseMenuMixin, FormCourseEventKwargsMixin, FormCourseKwargsMixin


class ClassLessonRedirectDetailMixin(object):
    def get_success_url(self):
       if self.context_object_name == 'classlessonblock':
           return reverse_lazy('coursebackend:classlesson:block',
                               kwargs={'course_slug': self.kwargs['course_slug'],
                                       'slug': self.kwargs['slug'],
                                       'pk': self.object.pk})
       elif self.context_object_name == 'classlesson':
           return reverse_lazy('coursebackend:classlesson:lesson',
                               kwargs={'course_slug': self.kwargs['course_slug'],
                                       'slug': self.kwargs['slug'],
                                       'pk': self.object.pk})
       elif self.context_object_name == 'classlessonstep':
           return reverse_lazy('coursebackend:classlesson:step',
                               kwargs={'course_slug': self.kwargs['course_slug'],
                                       'slug': self.kwargs['slug'],
                                       'pk': self.object.pk})


class ClassLessonRedirectListMixin(object):
    def get_success_url(self):
        return reverse_lazy('coursebackend:classlesson:start',
                            kwargs={'course_slug': self.kwargs['course_slug'],
                                    'slug': self.kwargs['slug']})


class ClassLessonBreadcrumbMixin(object):
    """
    get breadcrumbs for object
    """

    def get_context_data(self, **kwargs):
        context = super(ClassLessonBreadcrumbMixin, self).get_context_data(
            **kwargs)
        if 'object' in context:
            context['breadcrumbs'] = context[
                'object'].get_breadcrumbs_with_self
        return context


class ClassLessonBlockUpdateView(
    CourseMenuMixin,
    ClassLessonBreadcrumbMixin,
    FormValidMessageMixin,
    FormCourseKwargsMixin,
    ClassLessonRedirectDetailMixin,
    UpdateView):
    """
    Update a classlesson step
    """
    model = ClassLesson
    context_object_name = 'classlessonblock'
    form_class = ClassLessonBlockForm
    form_valid_message = "Der Unterrichtsblock wurde geändert!"


class ClassLessonUpdateView(
    CourseMenuMixin,
    ClassLessonBreadcrumbMixin,
    FormValidMessageMixin,
    FormCourseEventKwargsMixin,
    ClassLessonRedirectDetailMixin,
    UpdateView):
    """
    Update a classlesson
    """
    form_class = ClassLessonForm
    model = ClassLesson
    context_object_name = 'classlesson'
    form_valid_message = "Die Lektion wurde geändert!"


class ClassLessonStepUpdateView(
    CourseMenuMixin,
    ClassLessonBreadcrumbMixin,
    FormValidMessageMixin,
    FormCourseEventKwargsMixin,
    ClassLessonRedirectDetailMixin,
    UpdateView):
    """
    Update a classlesson step
    """
    model = ClassLesson
    context_object_name = 'classlessonstep'
    form_class = ClassLessonStepForm
    form_valid_message = "Der Lernabschnitt wurde geändert!"


class ClassLessonDeleteView(
    CourseMenuMixin,
    ClassLessonBreadcrumbMixin,
    FormValidMessageMixin,
    FormCourseEventKwargsMixin,
    ClassLessonRedirectListMixin,
    DeleteView):
    """
    Delete a classlesson
    """
    model = ClassLesson
    context_object_name = 'classlesson'
    form_valid_message = "Der Unterricht wurde gelöscht!"

    def get_context_data(self, **kwargs):
        context = super(ClassLessonDeleteView, self).get_context_data(**kwargs)
        context['nodes'] = context['object'].get_delete_tree
        return context


class ClassLessonBlockCreateView(
    CourseMenuMixin,
    ClassLessonRedirectDetailMixin,
    FormValidMessageMixin,
    FormView):
    """
    create lesson
    """
    form_class = ClassLessonBlockForm
    model = ClassLesson
    context_object_name ='classlessonblock'
    form_valid_message = "Der Block wurde angelegt!"

    def form_valid(self, form):
        courseevent = get_object_or_404(CourseEvent, slug=self.kwargs['course_slug'])
        self.object = ClassLesson.objects.create_classlessonblock(
            courseevent=courseevent,
            title=form.cleaned_data['title'],
            description=form.cleaned_data['description'],
            text=form.cleaned_data['text'],
            nr=form.cleaned_data['nr'],
        )
        return HttpResponseRedirect(self.get_success_url())


class ClassLessonCreateView(
    CourseMenuMixin,
    FormCourseEventKwargsMixin,
    ClassLessonRedirectDetailMixin,
    FormValidMessageMixin,
    FormView):
    """
    create lesson
    """
    form_class = ClassLessonForm
    model = Lesson
    context_object_name ='classlesson'
    form_valid_message = "Die Lektion wurde angelegt!"

    def form_valid(self, form):
        courseevent = get_object_or_404(CourseEvent, slug=self.kwargs['course_slug'])
        self.object = ClassLesson.objects.create_classlesson(
            courseevent=courseevent,
            title=form.cleaned_data['title'],
            description=form.cleaned_data['description'],
            text=form.cleaned_data['text'],
            parent=form.cleaned_data['parent'],
            nr=form.cleaned_data['nr'],
        )
        return HttpResponseRedirect(self.get_success_url())


class ClassLessonStepCreateView(
    CourseMenuMixin,
    FormCourseEventKwargsMixin,
    ClassLessonRedirectListMixin,
    FormValidMessageMixin,
    FormView):
    """
    create lesson step, special: add materials if requested
    """
    form_class = ClassLessonStepForm
    model = Lesson
    context_object_name ='lessonstep'
    form_valid_message = "Der Lernabschnitt wurde angelegt!"

    def form_valid(self, form):
        courseevent = get_object_or_404(CourseEvent, slug=self.kwargs['course_slug'])

        self.object = ClassLesson.objects.create_classstep(
            courseevent=courseevent,
            title=form.cleaned_data['title'],
            description=form.cleaned_data['description'],
            text=form.cleaned_data['text'],
            material=form.cleaned_data['material'],
            nr=form.cleaned_data['nr'],
            parent=form.cleaned_data['parent'],
            is_homework = form.cleaned_data['is_homework'],
        )
        return HttpResponseRedirect(self.get_success_url())
