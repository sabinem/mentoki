# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.shortcuts import get_object_or_404

from vanilla import TemplateView, CreateView, FormView

from apps_data.courseevent.models.forum import Forum, Thread, CourseEvent

from .mixins.base import ClassroomMenuMixin


class ForumStartView(ClassroomMenuMixin, TemplateView):
    """
    List all lesson blocks with lessons underneath
    """
    def get_context_data(self, **kwargs):
        context = super(ForumStartView, self).get_context_data(**kwargs)

        context['nodes'] = \
            Forum.objects.forums_published_in_courseevent(courseevent=context['courseevent'])

        return context


class ForumDetailView(ClassroomMenuMixin, TemplateView):
    """
    List all lesson blocks with lessons underneath
    """
    def get_context_data(self, **kwargs):
        context = super(ForumDetailView, self).get_context_data(**kwargs)

        forum = get_object_or_404(Forum, pk=self.kwargs['pk'])

        context['forum'] = forum
        context['breadcrumbs'] = forum.get_ancestors()
        context['nodes'] = forum.get_descendants()

        if forum.can_have_threads:
            context['threads'] = Thread.objects.filter(forum=forum)
        return context


class ForumRecentView(ClassroomMenuMixin, TemplateView):
    """
    List all lesson blocks with lessons underneath
    """
    def get_context_data(self, **kwargs):
        context = super(ForumRecentView, self).get_context_data(**kwargs)

        context['contributions'] = Thread.objects.recent_contributions(courseevent=context['courseevent'])
        return context