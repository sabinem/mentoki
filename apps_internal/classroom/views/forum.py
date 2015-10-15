# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.shortcuts import get_object_or_404

from django.views.generic import TemplateView

from apps_data.courseevent.models.forum import Forum, Thread, CourseEvent
from apps_data.courseevent.models.menu import ClassroomMenuItem

from .mixins.base import ClassroomMenuMixin


class ForumStartView(
    ClassroomMenuMixin,
    TemplateView):
    """
    shows all forums published in the classroom (published means a menu entry exists
    """
    def get_context_data(self, **kwargs):
        context = super(ForumStartView, self).get_context_data(**kwargs)

        context['nodes'] = Forum.objects.published_forums(
            courseevent=context['courseevent'])

        return context


class ForumDetailView(
    ClassroomMenuMixin,
    TemplateView):
    """
    show one forum
    """
    def get_context_data(self, **kwargs):
        context = super(ForumDetailView, self).get_context_data(**kwargs)

        forum = get_object_or_404(Forum, pk=self.kwargs['pk'])

        context['forum'] = forum
        context['breadcrumbs'] = forum.get_published_breadcrumbs_with_self
        context['nodes'] = forum.get_descendants()

        if forum.can_have_threads:
            context['threads'] = Thread.objects.filter(forum=forum)
        return context


class ForumRecentView(
    ClassroomMenuMixin,
    TemplateView):
    """
    show all recent forum contributions (threads and posts)
    """
    def get_context_data(self, **kwargs):
        context = super(ForumRecentView, self).get_context_data(**kwargs)

        context['contributions'] = Thread.objects.recent_published_contributions(
            courseevent=context['courseevent'])
        return context