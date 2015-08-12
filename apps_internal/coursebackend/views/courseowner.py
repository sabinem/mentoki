# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView, TemplateView, UpdateView

from apps_data.course.models.course import CourseOwner

from .mixins.base import CourseMenuMixin
from ..forms.courseowner import TeachersCourseProfileForm


class CourseOwnerListView(CourseMenuMixin, TemplateView):
    """
    Courseowner List
    """
    def get_context_data(self, **kwargs):
        context = super(CourseOwnerListView, self).get_context_data(**kwargs)

        context['courseowners'] = CourseOwner.objects.teachers_courseinfo_all(course=context['course'])

        return context


class CourseOwnerDetailView(CourseMenuMixin, DetailView):
    """
    Courseowner List
    """
    model = CourseOwner
    context_object_name = 'courseowner'



class CourseOwnerUpdateView(CourseMenuMixin, UpdateView):
    """
    Courseowner Update
    """
    model = CourseOwner
    context_object_name = 'courseowner'
    form_class = TeachersCourseProfileForm
    form_valid_message="Das Kursleiterprofil wurde geändert!"

    def get_success_url(self):
        self.messages.info(self.success_msg)
        return reverse_lazy('coursebackend:courseowner:list',
                            kwargs={"course_slug": self.kwargs['course_slug'],})

