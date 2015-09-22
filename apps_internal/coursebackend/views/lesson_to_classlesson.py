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

from apps_data.lesson.utils.lessoncopy import copy_lesson_selected

from .mixins.base import CourseMenuMixin, FormCourseEventKwargsMixin, FormCourseKwargsMixin
from .classlessonupdate import ClassLessonRedirectListMixin


class CopyBlockListView(
    CourseMenuMixin,
    TemplateView):
    """
    Lists all lessons and provide the option to copy them as classlessons
    for a courseevent
    :param slug: of courseevent
    :param course_slug: slug of course
    :return: lessons: all lessons of the course
             copied_lesson_ids: ids of all lessons of the course that have
             already been copied
    """

    def get_context_data(self, **kwargs):
        context = super(CopyBlockListView, self).get_context_data(**kwargs)

        context['blocks'] = \
            Lesson.objects.blocks_for_course(course=context['course'])
        print context['blocks']
        return context


class CopyLessonView(
    CourseMenuMixin,
    FormValidMessageMixin,
    ClassLessonRedirectListMixin,
    FormView):
    """
    Copy (and update or create) parts of a lesson into the class as classlesson
    """
    form_class = LessonCopyForm
    form_valid_message = "Die Lektion wurde wie gewünscht kopiert!"

    def get_form_kwargs(self):
        lesson_pk = self.kwargs['pk']
        kwargs = super(CopyLessonView, self).get_form_kwargs()
        kwargs['lesson_pk'] = lesson_pk
        return kwargs

    def form_valid(self, form):
        courseevent = get_object_or_404(CourseEvent, slug=self.kwargs['slug'])
        copied = copy_lesson_selected(self,
                                      lesson=form.lesson,
                                      lessonsteps=form.cleaned_data[
                                          'copy_lessonsteps'],
                                      copy_lesson=form.cleaned_data[
                                          'copy_lesson'],
                                      courseevent=courseevent
                                      )

        return super(CopyLessonView, self).form_valid(form)


class ClassLessonBLockUnlockView(
    CourseMenuMixin,
    FormValidMessageMixin,
    FormCourseEventKwargsMixin,
    ClassLessonRedirectListMixin,
    DeleteView):
    """
    Delete a classlesson
    """
    model = ClassLesson
    context_object_name = 'classlessonblock'
    form_valid_message = "Der Block wurde abgekoppelt!"

    def get_context_data(self, **kwargs):
        context = super(ClassLessonBLockUnlockView, self).get_context_data(**kwargs)
        context['nodes'] = context['object'].get_delete_tree
        return context

    def delete(self, request, *args, **kwargs):
        """
        Calls the delete() method on the fetched object and then
        redirects to the success URL.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.cut_block_connection()
        return HttpResponseRedirect(success_url)