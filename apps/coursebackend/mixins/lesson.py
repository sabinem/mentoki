# -*- coding: utf-8 -*-

from apps.course.models import Lesson

from ..mixins import CourseMenuMixin


class LessonsMenuMixin(CourseMenuMixin):

    def get_context_data(self, **kwargs):
        context = super(LessonsMenuMixin, self).get_context_data(**kwargs)

        return context


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