# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.http import HttpResponseRedirect
from django.views.generic import DeleteView, TemplateView

from braces.views import FormValidMessageMixin

from apps_data.lesson.models.classlesson import ClassLesson
from apps_data.lesson.models.lesson import Lesson

from .mixins.base import CourseMenuMixin, FormCourseEventKwargsMixin, FormCourseKwargsMixin
from .classlessonupdate import ClassLessonRedirectListMixin


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
        context['copied_blocks'] = \
            ClassLesson.objects.copied_blocks(courseevent=context['courseevent'])
        context['uncopied_blocks'] = \
            Lesson.objects.uncopied_blocks(
                courseevent=context['courseevent'])
        context['independent_blocks'] = \
            ClassLesson.objects.independent_blocks(
                courseevent=context['courseevent'])
        print context
        return context