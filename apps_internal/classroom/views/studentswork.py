# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, DetailView, UpdateView, FormView, DeleteView

from apps_data.courseevent.models.homework import StudentsWork
from apps_core.email.utils.homework import send_work_published_notification
from apps_data.courseevent.models.courseevent import CourseEvent
from apps_internal.coursebackend.views.mixins.base import FormCourseEventKwargsMixin

from .mixins.base import ClassroomMenuMixin
from .classlessonstepwork import LessonStepContextMixin, StudentsWorkRedirectMixin
from ..forms.studentswork import StudentWorkCreateForm


class StudentsWorkListPrivateView(
    ClassroomMenuMixin,
    TemplateView):
    """
    list all works where student is in the team
    """
    def get_context_data(self, **kwargs):
        context = super(StudentsWorkListPrivateView, self).get_context_data(**kwargs)

        context['studentsworks'] = \
            StudentsWork.objects.unpublished_homework_courseevent(user=self.request.user,
                                                      courseevent=context['courseevent'])
        return context


class StudentsWorkListPublicView(
    ClassroomMenuMixin,
    TemplateView):
    """
    list all works where student is in the team
    """
    def get_context_data(self, **kwargs):
        context = super(StudentsWorkListPublicView, self).get_context_data(**kwargs)

        context['studentsworks'] = StudentsWork.objects.turnedin_homework_courseevent(
                                                      user=self.request.user,
                                                      courseevent=context['courseevent'])
        return context


class StudentsWorkCreateView(
    ClassroomMenuMixin,
    FormCourseEventKwargsMixin,
    StudentsWorkRedirectMixin,
    FormView):
    """
    creates a students work object
    """
    model = StudentsWork
    form_class = StudentWorkCreateForm
    context_object_name ='studentswork'

    def form_valid(self, form):
        print self.kwargs['slug']
        courseevent = get_object_or_404(CourseEvent, slug=self.kwargs['slug'])
        print courseevent
        self.object = StudentsWork.objects.create(
            courseevent=courseevent,
            homework=form.cleaned_data['homework'],
            published=form.cleaned_data['published'],
            text=form.cleaned_data['text'],
            title=form.cleaned_data['title'],
            user=self.request.user)
        return HttpResponseRedirect(self.get_success_url())