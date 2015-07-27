# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404

from apps_data.course.models import Lesson

from ..mixins import CourseMenuMixin


class CourseFormMixin(CourseMenuMixin):

    def get_form_kwargs(self):

        course_slug = self.kwargs['course_slug']

        kwargs = super(CourseFormMixin, self).get_form_kwargs()

        kwargs['course_slug'] = course_slug
        return kwargs

    def form_valid(self, form, **kwargs):
        context = self.get_context_data(**kwargs)
        form.instance.course = context['course']
        return super(CourseFormMixin, self).form_valid(form)


class LessonMixin(CourseMenuMixin):

    def get_context_data(self, **kwargs):
        context = super(LessonMixin, self).get_context_data(**kwargs)

        start_node = get_object_or_404(Lesson, pk=self.kwargs['pk'])

        context['start_node'] = start_node

        context['root_node'] = start_node.get_root()

        context['next_node'] = start_node.get_next_sibling()

        context['previous_node'] = start_node.get_previous_sibling()

        context['breadcrumbs'] = start_node.get_ancestors()

        #context['nodes'] = start_node.get_descendants(include_self=True).prefetch_related('material')
        context['nodes'] = start_node.get_tree_with_material

        return context


class LessonFormMixin(CourseFormMixin):

    def get_context_data(self, **kwargs):
        context = super(LessonFormMixin, self).get_context_data(**kwargs)

        context['breadcrumbs'] = self.lesson.get_ancestors()
        print context['breadcrumbs']

        return context