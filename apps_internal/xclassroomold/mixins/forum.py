# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404

from apps_data.courseevent.models import Forum

from ..mixins import CourseMenuMixin


class ForumMixin(CourseMenuMixin):

    def get_context_data(self, **kwargs):
        context = super(ForumMixin, self).get_context_data(**kwargs)

        start_node = get_object_or_404(Forum, pk=self.kwargs['pk'])

        context['start_node'] = start_node

        context['root_node'] = start_node.get_root()

        context['next_node'] = start_node.get_next_sibling()

        context['previous_node'] = start_node.get_previous_sibling()

        context['breadcrumbs'] = start_node.get_ancestors()

        return context

