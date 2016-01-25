# coding: utf-8
"""
List views for Lessons
"""

from __future__ import unicode_literals, absolute_import

from django.views.generic import TemplateView

from apps_data.lesson.models.lesson import Lesson

from ..mixins.base import CourseMenuMixin


class BlockListView(
    CourseMenuMixin,
    TemplateView):
    """
    List everything for a course: get the complete tree with material
    :param course_slug: slug of course
    :return: nodes: all complete trees for course
    """

    def get_context_data(self, **kwargs):
        context = super(BlockListView, self).get_context_data(**kwargs)
        context['nodes'] = Lesson.objects.start_tree_for_course(course=context['course'])
        context['blocks'] = Lesson.objects.blocks_for_course(course=context['course'])
        self.request.session['last_url'] = self.request.path
        return context


class BlockLessonsView(
    CourseMenuMixin,
    TemplateView):
    """
    List everything for a course: get the complete tree with material
    :param course_slug: slug of course
    :return: nodes: all complete trees for course
    """

    def get_context_data(self, **kwargs):
        context = super(BlockLessonsView, self).get_context_data(**kwargs)

        context['nodes'] = Lesson.objects.start_tree_for_course(course=context['course'])
        self.request.session['last_url'] = self.request.path
        return context



class HomeworkListView(
    CourseMenuMixin,
    TemplateView):
    """
    List everything for a course: get the complete tree with material
    :param course_slug: slug of course
    :return: nodes: all complete trees for course
    """

    def get_context_data(self, **kwargs):
        context = super(HomeworkListView, self).get_context_data(**kwargs)
        self.request.session['last_url'] = self.request.path
        context['homeworks'] = Lesson.objects.homeworks(course=context['course'])
        return context

