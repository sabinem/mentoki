# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.views.generic import TemplateView

from apps_data.lesson.models.classlesson import ClassLesson

from ..mixins.base import CourseMenuMixin

import logging

logger = logging.getLogger('activity.lessonview')


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
        courseevent = context['courseevent']
        self.request.session['last_url'] = self.request.path
        logger.info('Alle Kurslektionen werden gesucht zu Kurs [%s]' % courseevent)
        context['nodes'] = \
            ClassLesson.objects.complete_tree_for_courseevent(
                courseevent=courseevent)
        return context


