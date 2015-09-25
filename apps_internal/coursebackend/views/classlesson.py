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


class ClassLessonStartView(
    CourseMenuMixin,
    TemplateView):
    """
    complete tree for courseevent:
    :param slug: of courseevent
    :param course_slug: slug of course
    :return: nodes: complete tree for the courseevent including blocks and material
    """

    def get_context_data(self, **kwargs):
        context = super(ClassLessonStartView, self).get_context_data(**kwargs)

        context['nodes'] = \
            ClassLesson.objects.complete_tree_for_courseevent(
                courseevent=context['courseevent'])
        print context['nodes']
        print context['courseevent']
        return context


class ClassBlockDetailView(
    CourseMenuMixin,
    DetailView):
    """
    detail block for classlessons:
    :param slug: of courseevent
    :param course_slug: slug of course
    :param pk: of lessonblock
    :return: lessonblock: classlesson block instance
    :return: previous_node: previous classblock within courseevent
    :return: next_node: next classblock within courseevent
    :return: breadcrumbs: ancestors including self instance
    :return: nodes: tree underneath of block instance without material
    """
    model = ClassLesson
    context_object_name = 'classlessonblock'

    def get_context_data(self, **kwargs):
        context = super(ClassBlockDetailView, self).get_context_data(**kwargs)

        classlessonblock = context['classlessonblock']

        context['next_node'] = classlessonblock.get_next_sibling_in_courseevent
        context[
            'previous_node'] = classlessonblock.get_previous_sibling_in_courseevent
        context['breadcrumbs'] = classlessonblock.get_breadcrumbs_with_self

        context['nodes'] = classlessonblock.get_tree_without_self_without_material

        return context


class ClassLessonDetailView(
    CourseMenuMixin,
    DetailView):
    """
    detail for classlesson
    :param slug: of courseevent
    :param course_slug: slug of course
    :param pk: of classlesson
    :return: lesson: classlesson instance
    :return: previous_node: previous classlesson within courseevent
    :return: next_node: next classlesson within courseevent
    :return: breadcrumbs: ancestors including self instance
    :return: nodes: tree underneath of lesson instance with material
    """
    model = ClassLesson
    context_object_name = 'classlesson'

    def get_context_data(self, **kwargs):
        context = super(ClassLessonDetailView, self).get_context_data(**kwargs)

        classlesson = context['classlesson']

        context['next_node'] = classlesson.get_next_sibling_in_courseevent
        context['previous_node'] = classlesson.get_previous_sibling_in_courseevent
        context['breadcrumbs'] = classlesson.get_breadcrumbs_with_self

        context['nodes'] = classlesson.get_tree_without_self_with_material
        print context
        return context


class ClassStepDetailView(
    CourseMenuMixin,
    DetailView):
    """
    Detail ClassLessonstep
    :param pk: of class lessonstep
    :param course_slug: slug of course
    :return: lessonstep: class lessonstep instance
    :return: previous_node: previous class lessonstep within classlesson
    :return: next_node: next classlessonstep within classlesson
    :return: breadcrumbs: ancestors including lessonstep instance
    """
    model = ClassLesson
    context_object_name = 'classlessonstep'

    def get_context_data(self, **kwargs):
        context = super(ClassStepDetailView, self).get_context_data(**kwargs)

        classlessonstep = context['classlessonstep']

        context['next_node'] = classlessonstep.get_next_sibling()
        context['previous_node'] = classlessonstep.get_previous_sibling()
        context['breadcrumbs'] = classlessonstep.get_breadcrumbs_with_self

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

        context['homeworks'] = ClassLesson.objects.homeworks(courseevent=context['courseevent'])

        return context


