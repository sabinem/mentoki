# coding: utf-8

from __future__ import unicode_literals, absolute_import

from vanilla import TemplateView

from .mixins.lesson import LessonMixin


class LessonDetailView(LessonMixin, TemplateView):
    """
    List all lesson-steps of a lesson
    """
    template_name = 'classroom/lesson/lesson.html'


class StepDetailView(LessonMixin, TemplateView):
    """
    Shows one lesson-step
    """
    template_name = 'classroom/lesson/lesson_step.html'


