# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.http import HttpResponseRedirect
from django.views.generic import DeleteView, TemplateView

from braces.views import FormValidMessageMixin, MessageMixin

from apps_data.lesson.models.classlesson import ClassLesson
from apps_data.lesson.models.lesson import Lesson

from ..mixins.base import CourseMenuMixin, FormCourseEventKwargsMixin, FormCourseKwargsMixin
from .mixin import ClassLessonSuccessUpdateUrlMixin

import logging

logger = logging.getLogger('activity.lessoncopy')


class ClassLessonBLockUnlockView(
    CourseMenuMixin,
    FormValidMessageMixin,
    FormCourseEventKwargsMixin,
    ClassLessonSuccessUpdateUrlMixin,
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
    MessageMixin,
    CourseMenuMixin,
    TemplateView):
    """
    Lists all blocks for copying from the course into the
    courseevent.
    If they have already been copied, they can be unlocked, to develop
    independently form the course blocks.
    Blocks that have already been unlocked are also listed.
    :param slug: of courseevent
    :param course_slug: slug of course
    :return: lessonblocks: all lessonblocks of the course
             along with buttons to copy or split from the course block
    """

    def get_context_data(self, **kwargs):
        context = super(CopyBlockListView, self).get_context_data(**kwargs)
        context['copied_blocks'] = \
            ClassLesson.objects.\
                copied_blocks(courseevent=context['courseevent'])
        context['uncopied_blocks'] = \
            Lesson.objects.\
                uncopied_blocks(courseevent=context['courseevent'])
        context['independent_blocks'] = \
            ClassLesson.objects.\
                independent_blocks(courseevent=context['courseevent'])
        return context