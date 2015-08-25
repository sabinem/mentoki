# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import DetailView, TemplateView, UpdateView, DeleteView, FormView

from braces.views import FormValidMessageMixin

from apps_data.courseevent.models.homework import Homework
from apps_data.courseevent.models.courseevent import CourseEvent

from .mixins.base import CourseMenuMixin, FormCourseEventKwargsMixin
from ..forms.homework import HomeworkForm


class HomeworkRedirectMixin(object):
    def get_success_url(self):
       """
       for create update and delete view
       """
       print "i am here"
       print object
       return reverse_lazy('coursebackend:homework:list',
                           kwargs={'slug': self.kwargs['slug'],
                                   'course_slug': self.kwargs['course_slug']})


class HomeworkListView(
    CourseMenuMixin,
    TemplateView):
    """
    Homework List
    """
    def get_context_data(self, **kwargs):
        context = super(HomeworkListView, self).get_context_data(**kwargs)

        context['homeworks'] = \
            Homework.objects.homeworks_for_courseevent(courseevent=context['courseevent'])

        return context


class HomeworkDetailView(
    CourseMenuMixin,
    DetailView):
    """
    Homework Detail
    """
    model = Homework
    context_object_name ='homework'


class HomeworkUpdateView(
    CourseMenuMixin,
    FormCourseEventKwargsMixin,
    FormValidMessageMixin,
    HomeworkRedirectMixin,
    UpdateView):
    """
    Homework Update
    """
    model = Homework
    form_class = HomeworkForm
    context_object_name ='homework'
    form_valid_message = "Die Aufgabe wurde geändert!"


class HomeworkDeleteView(
    CourseMenuMixin,
    FormValidMessageMixin,
    HomeworkRedirectMixin,
    DeleteView):
    """
    Homework Delete
    """
    model = Homework
    context_object_name ='homework'
    form_valid_message = "Die Aufgabe wurde gelöscht!"


class HomeworkCreateView(
    CourseMenuMixin,
    FormCourseEventKwargsMixin,
    FormValidMessageMixin,
    HomeworkRedirectMixin,
    FormView):
    """
    Homework Create
    """
    model = Homework
    form_class = HomeworkForm
    context_object_name ='homework'
    form_valid_message = "Die Aufgabe wurde angelegt!"


    def form_valid(self, form):
        courseevent = get_object_or_404(CourseEvent, slug=self.kwargs['slug'])
        Homework.objects.create(
            courseevent=courseevent,
            classlesson=form.cleaned_data['classlesson'],
            text=form.cleaned_data['text'],
            title=form.cleaned_data['title'],
            due_date=form.cleaned_data['due_date'],
        )

        return HttpResponseRedirect(self.get_success_url())



