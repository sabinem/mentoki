# coding: utf-8

"""
Lesson Detail views
"""

from __future__ import unicode_literals, absolute_import

from django.views.generic import DetailView

from apps_data.lesson.models.lesson import Lesson
from apps_data.lesson.constants import LessonType

from ..mixins.base import CourseMenuMixin


class BlockDetailView(
    CourseMenuMixin,
    DetailView):
    """
    gets tree underneath a block, get neighbouring blocks within the course and get breadcrumbs
    :param pk: of lessonblock
    :param course_slug: slug of course
    :return: lessonblock: block instance
    :return: previous_node: previous block within course
    :return: next_node: next block within course
    :return: breadcrumbs: ancestors including block instance
    :return: nodes: tree underneath of block instance without material
    """
    model = Lesson
    context_object_name ='lessonblock'

    def get_context_data(self, **kwargs):
        context = super(BlockDetailView, self).get_context_data(**kwargs)
        lessonblock = context['lessonblock']
        self.request.session['last_url'] = self.request.path
        self.request.session['last_lesson_type'] = LessonType.BLOCK
        self.request.session['last_lesson_pk'] = lessonblock.pk
        context['next_node'] = lessonblock.get_next_sibling()
        context['previous_node'] = lessonblock.get_previous_sibling()
        context['breadcrumbs'] = lessonblock.get_breadcrumbs_with_self()
        context['nodes'] = lessonblock.get_tree_without_self_without_material
        return context


class LessonDetailView(
    CourseMenuMixin,
    DetailView):
    """
    Detail Lesson with Lessonsteps underneath
    :param pk: of lesson
    :param course_slug: slug of course
    :return: lesson: lesson instance
    :return: previous_node: previous lesson within block
    :return: next_node: next lesson within block
    :return: breadcrumbs: ancestors including lesson instance
    :return: nodes: tree underneath of lesson instance with material
    """
    model = Lesson
    context_object_name ='lesson'

    def get_context_data(self, **kwargs):
        context = super(LessonDetailView, self).get_context_data(**kwargs)

        lesson = context['lesson']
        self.request.session['last_url'] = self.request.path
        self.request.session['last_lesson_type'] = LessonType.LESSON
        self.request.session['last_lesson_pk'] = lesson.pk
        context['next_node'] = lesson.get_next_sibling()
        context['previous_node'] = lesson.get_previous_sibling()
        context['breadcrumbs'] = lesson.get_breadcrumbs_with_self
        context['nodes'] = lesson.get_tree_without_self_with_material
        return context


class StepDetailView(CourseMenuMixin, DetailView):
    """
    Detail Lessonstep
    :param pk: of lessonstep
    :param course_slug: slug of course
    :return: lessonstep: lessonstep instance
    :return: previous_node: previous lessonstep within lesson
    :return: next_node: next lesson within lesson
    :return: breadcrumbs: ancestors including lessonstep instance
    """
    model = Lesson
    context_object_name ='lessonstep'

    def get_context_data(self, **kwargs):
        context = super(StepDetailView, self).get_context_data(**kwargs)

        lessonstep = context['lessonstep']
        self.request.session['last_url'] = self.request.path
        self.request.session['last_lesson_type'] = LessonType.LESSONSTEP
        self.request.session['last_lesson_pk'] = lessonstep.pk
        context['next_node'] = lessonstep.get_next_sibling()
        context['previous_node'] = lessonstep.get_previous_sibling()
        context['breadcrumbs'] = lessonstep.get_breadcrumbs_with_self

        return context