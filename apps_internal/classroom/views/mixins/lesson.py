# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404

from apps_data.course.models.lesson import Lesson

from .base import ClassroomMenuMixin


class LessonMixin(ClassroomMenuMixin):

    def get_context_data(self, **kwargs):
        context = super(LessonMixin, self).get_context_data(**kwargs)

        start_node = get_object_or_404(Lesson, pk=self.kwargs['pk'])

        context['start_lesson'] = start_node

        context['next_node'] = start_node.get_next_sibling()

        context['previous_node'] = start_node.get_previous_sibling()

        context['breadcrumbs'] = start_node.get_ancestors()

        context['nodes'] = start_node.get_tree_with_material

        return context

