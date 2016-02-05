# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.views.generic import DetailView

from apps_data.lesson.models.classlesson import ClassLesson

from ..mixins.base import CourseMenuMixin
import logging

logger = logging.getLogger('activity.lessonview')



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
        self.request.session['last_url'] = self.request.path

        context['next_node'] = classlessonblock.get_next_sibling_in_courseevent
        context[
            'previous_node'] = classlessonblock.get_previous_sibling_in_courseevent
        context['breadcrumbs'] = classlessonblock.get_breadcrumbs_with_self

        context['nodes'] = classlessonblock.get_tree_with_self_with_material

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
        self.request.session['last_url'] = self.request.path
        context['next_node'] = classlesson.get_next_sibling_in_courseevent
        context['previous_node'] = classlesson.get_previous_sibling_in_courseevent
        context['breadcrumbs'] = classlesson.get_breadcrumbs_with_self

        context['nodes'] = classlesson.get_tree_with_self_with_material
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
        self.request.session['last_url'] = self.request.path
        context['next_node'] = classlessonstep.get_next_sibling()
        context['previous_node'] = classlessonstep.get_previous_sibling()
        context['breadcrumbs'] = classlessonstep.get_breadcrumbs_with_self

        return context