# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, FormView

import floppyforms.__future__ as forms
from froala_editor.widgets import FroalaEditor

from apps_data.courseevent.models.homework import StudentsWork
from apps_data.courseevent.models.courseevent import CourseEvent
from apps_internal.coursebackend.views.mixins.base import FormCourseEventKwargsMixin
from apps_data.courseevent.models.menu import ClassroomMenuItem

from .mixins.base import ClassroomMenuMixin
from .classlessonstepwork import StudentsWorkRedirectMixin


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


class StudentWorkCreateForm(forms.ModelForm):
    text = forms.CharField(widget=FroalaEditor)

    class Meta:
        model = StudentsWork
        fields = ('homework', 'title', 'text', 'published')

    def __init__(self, *args, **kwargs):
        courseevent_slug = kwargs.pop('courseevent_slug', None)
        self.courseevent = get_object_or_404(CourseEvent, slug=courseevent_slug)

        super(StudentWorkCreateForm, self).__init__(*args, **kwargs)

        self.fields["homework"].queryset = \
            ClassroomMenuItem.objects.homeworks_published_in_class(courseevent=self.courseevent)
        self.fields['homework'].empty_label = None


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