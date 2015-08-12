# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import DetailView, TemplateView, UpdateView, DeleteView, FormView

from braces.views import FormValidMessageMixin

from apps_data.courseevent.models.homework import Homework
from apps_data.courseevent.models.courseevent import CourseEvent
from apps_data.courseevent.models.courseevent import Course
from apps_data.course.models.lesson import Lesson

from .mixins.base import CourseMenuMixin, FormCourseKwargsMixin
from ..forms.homework import HomeworkForm


class ListRedirectMixin(object):

    def get_success_url(self):
       """
       for create update and delete view
       """
       return reverse_lazy('coursebackend:homework:list',
                           kwargs={'slug': self.kwargs['slug'],
                                   'course_slug': self.kwargs['course_slug']})


class HomeworkListView(CourseMenuMixin, TemplateView):
    """
    Homework List
    """
    def get_context_data(self, **kwargs):
        context = super(HomeworkListView, self).get_context_data(**kwargs)

        context['homeworks_published'] = \
            Homework.objects.published_homework_for_courseevent(courseevent=context['courseevent'])
        context['homeworks_unpublished'] = \
            Homework.objects.unpublished_per_courseevent(courseevent=context['courseevent'])

        return context


class HomeworkDetailView(CourseMenuMixin, DetailView):
    """
    Homework Detail
    """
    model = Homework
    context_object_name ='homework'


class HomeworkUpdateView(CourseMenuMixin, FormCourseKwargsMixin,
                         FormValidMessageMixin, ListRedirectMixin, UpdateView):
    """
    Homework Update
    """
    model = Homework
    form_class = HomeworkForm
    context_object_name ='homework'
    form_valid_message = "Die Aufgabe wurde geändert!"


class HomeworkDeleteView(CourseMenuMixin, FormValidMessageMixin, ListRedirectMixin, DeleteView):
    """
    Homework Delete
    """
    model = Homework
    context_object_name ='homework'
    form_valid_message = "Die Aufgabe wurde gelöscht!"


class HomeworkCreateView(CourseMenuMixin, FormCourseKwargsMixin,
                         FormValidMessageMixin, ListRedirectMixin, FormView):
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
            lesson=form.cleaned_data['lesson'],
            text=form.cleaned_data['text'],
            title=form.cleaned_data['title'],
            due_date=form.cleaned_data['due_date'],
        )

        return HttpResponseRedirect(self.get_success_url())



