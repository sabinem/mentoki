# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, DetailView, UpdateView, FormView, DeleteView

from apps_data.courseevent.models.homework import StudentsWork
from apps_data.courseevent.models.courseevent import CourseEvent
from apps_internal.coursebackend.views.mixins.base import FormCourseEventKwargsMixin

from .mixins.base import ClassroomMenuMixin
from ..forms.studentswork import StudentWorkCreateForm, StudentWorkAddTeamForm, StudentWorkUpdateForm


class StudentsWorkRedirectMixin(
    object):
    """
    redirects after successful form submit
    """
    def get_success_url(self):
       return reverse_lazy('classroom:studentswork:list',
                           kwargs={'slug': self.kwargs['slug']})


class StudentsWorkListView(
    ClassroomMenuMixin,
    TemplateView):
    """
    list all works where student is in the team
    """
    def get_context_data(self, **kwargs):
        context = super(StudentsWorkListView, self).get_context_data(**kwargs)

        context['studentsworks'] = StudentsWork.objects.mywork(user=self.request.user,
                                                              courseevent=context['courseevent'])
        return context


class StudentsWorkDetailView(
    ClassroomMenuMixin,
    DetailView):
    """
    shows details of studentswork object
    """
    model = StudentsWork
    context_object_name ='studentswork'


class StudentsWorkUpdateView(
    ClassroomMenuMixin,
    StudentsWorkRedirectMixin,
    UpdateView):
    """
    updates a students work object
    """
    model = StudentsWork
    form_class = StudentWorkUpdateForm
    context_object_name ='studentswork'


class StudentsWorkDeleteView(
    ClassroomMenuMixin,
    StudentsWorkRedirectMixin,
    DeleteView):
    """
    deletes a students work object
    """
    model = StudentsWork
    context_object_name ='studentswork'


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
        courseevent = get_object_or_404(CourseEvent, slug=self.kwargs['slug'])
        StudentsWork.objects.create(
            courseevent=courseevent,
            homework=form.cleaned_data['homework'],
            text=form.cleaned_data['text'],
            title=form.cleaned_data['title'],
            user=self.request.user)

        return HttpResponseRedirect(self.get_success_url())


class StudentsWorkAddTeamView(
    ClassroomMenuMixin,
    FormCourseEventKwargsMixin,
    StudentsWorkRedirectMixin,
    UpdateView):
    """
    adds new team members to students work object
    """
    model = StudentsWork
    form_class = StudentWorkAddTeamForm
    context_object_name = 'studentswork'

