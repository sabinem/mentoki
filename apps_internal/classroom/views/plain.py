# coding: utf-8

from __future__ import unicode_literals, absolute_import

from vanilla import TemplateView

from apps_data.courseevent.models.forum import Forum, Thread, Post
from apps_data.courseevent.models.homework import Homework, StudentsWork
from apps_data.lesson.models.lesson import Lesson
from apps_data.courseevent.models.menu import ClassroomMenuItem

from .mixins.base import ClassroomMenuMixin


class PlainListView(ClassroomMenuMixin, TemplateView):
    """
    List all lesson blocks with lessons underneath
    """
    def get_context_data(self, **kwargs):
        context = super(PlainListView, self).get_context_data(**kwargs)

        context['forums'] = \
            Forum.objects.forums_published_in_courseevent(courseevent=context['courseevent'])

        context['homeworks'] = Homework.objects.published_homework_for_courseevent(courseevent=context['courseevent'])

        return context

