# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

from vanilla import TemplateView, DetailView, UpdateView, FormView, DeleteView

from apps_data.courseevent.models.homework import Homework
from apps_data.courseevent.models.courseevent import CourseEvent
from apps_data.courseevent.models.courseevent import Course
from apps_data.course.models.lesson import Lesson

from .mixins.base import CourseMenuMixin
from ..forms.homework import HomeworkForm


class HomeworkMixin(CourseMenuMixin):

    def get_success_url(self):
       """
       for create update and delete view
       """
       return reverse_lazy('coursebackend:homework:list',
                           kwargs={'slug': self.kwargs['slug'],
                                   'course_slug': self.kwargs['course_slug']})


class HomeworkListView(HomeworkMixin, TemplateView):
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


class HomeworkDetailView(HomeworkMixin, DetailView):
    """
    Homework Detail
    """
    model = Homework
    lookup_field = 'pk'
    context_object_name ='homework'


class HomeworkUpdateView(HomeworkMixin, UpdateView):
    """
    Homework Update
    """
    model = Homework
    form_class = HomeworkForm
    lookup_field = 'pk'
    context_object_name ='homework'


class HomeworkDeleteView(HomeworkMixin, DeleteView):
    """
    Homework Delete
    """
    model = Homework
    lookup_field = 'pk'
    context_object_name ='homework'


class HomeworkCreateView(HomeworkMixin, FormView):
    """
    Homework Create
    """
    model = HomeworkMixin
    form_class = HomeworkForm
    context_object_name ='homework'
    form_class = HomeworkForm

    def get(self, request, *args, **kwargs):
        course = get_object_or_404(Course,slug=self.kwargs['course_slug'])
        form = self.get_form()
        form.fields['lesson'].queryset = \
            Lesson.objects.lessons_for_course(course=course)
        context = self.get_context_data(form=form)
        return self.render_to_response(context)


    def form_valid(self, form):
        courseevent = get_object_or_404(CourseEvent, slug=self.kwargs['slug'])
        Homework.objects.create(
            courseevent=courseevent,
            lesson=form.cleaned_data['lesson'],
            text=form.cleaned_data['text'],
            title=form.cleaned_data['title'],
            due_date=form.cleaned_data['due_date'],
            published=form.cleaned_data['published']
        )

        return HttpResponseRedirect(self.get_success_url())



