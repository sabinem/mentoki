# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, UpdateView, DetailView

from apps_data.courseevent.models.homework import StudentsWork, Homework

from .mixins.base import ClassroomMenuMixin
from ..forms.studentswork import StudentWorkCommentForm


class HomeWorkContextMixin(object):
    """
    adds the homework to the context
    """
    def get_context_data(self, **kwargs):
        context = super(HomeWorkContextMixin, self).get_context_data(**kwargs)

        context['homework'] = get_object_or_404(Homework, pk=self.kwargs['pk'])
        return context


class HomeWorkListView(
    ClassroomMenuMixin,
    HomeWorkContextMixin,
    TemplateView):
    """
    List all students works for a homework
    """
    def get_context_data(self, **kwargs):
        context = super(HomeWorkListView, self).get_context_data(**kwargs)
        context['studentsworks'] = \
            StudentsWork.objects.turnedin_homework(homework=context['homework'])

        return context


class StudentsWorkDetailView(
    ClassroomMenuMixin,
    HomeWorkContextMixin,
    DetailView):
    """
    shows detail of a students work, that is published in the homework section
    """
    model = StudentsWork
    pk_url_kwarg = 'work_pk'
    context_object_name ='studentswork'


class StudentsWorkCommentView(
    ClassroomMenuMixin,
    HomeWorkContextMixin,
    UpdateView):
    """
    provides a form for the rest of the class and the teacher to comment on a students work
    """
    model = StudentsWork
    pk_url_kwarg = 'work_pk'
    context_object_name ='studentswork'
    form_class = StudentWorkCommentForm

    def get_success_url(self):
       return reverse_lazy('classroom:homework:studentswork',
                           kwargs={'slug': self.kwargs['slug'], 'pk':self.kwargs['pk'],
                                   'work_pk':self.kwargs['work_pk']})

