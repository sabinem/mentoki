# coding: utf-8

from __future__ import unicode_literals, absolute_import

from vanilla import TemplateView

from apps_data.courseevent.models.forum import Forum

from ..mixins.base import CourseMenuMixin
from ..mixins.forum import ForumMixin


class ForumStartView(CourseMenuMixin, TemplateView):
    """
    List all lesson blocks with lessons underneath
    """
    template_name = 'coursebackend/forum/start.html'

    def get_context_data(self, **kwargs):
        context = super(ForumStartView, self).get_context_data(**kwargs)

        context['nodes'] = Forum.objects.forums_for_courseevent(courseevent=context['courseevent'])
        print context['nodes']

        return context


class ForumDetailView(ForumMixin, TemplateView):
    """
    List all lesson blocks with lessons underneath
    """
    template_name = 'coursebackend/forum/detail.html'