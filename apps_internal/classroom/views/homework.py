# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404

from vanilla import TemplateView, UpdateView, DetailView

from apps_data.courseevent.models.homework import StudentsWork, Homework

from .mixins.base import ClassroomMenuMixin
from ..forms.studentswork import StudentWorkCommentForm


class HomeWorkMixin(ClassroomMenuMixin):

    def get_success_url(self):
       """
       for create update and delete view
       """
    def get_context_data(self, **kwargs):
        context = super(HomeWorkMixin, self).get_context_data(**kwargs)

        context['homework'] = get_object_or_404(Homework, pk=self.kwargs['pk'])
        return context


class HomeWorkListView(HomeWorkMixin, TemplateView):
    """
    List all students works for a homework
    """
    template_name = 'classroom/homework/pages/list.html'

    def get_context_data(self, **kwargs):
        context = super(HomeWorkListView, self).get_context_data(**kwargs)
        context['studentsworks'] = \
            StudentsWork.objects.turnedin_homework(homework=context['homework'])

        return context


class StudentsWorkDetailView(HomeWorkMixin, DetailView):
    """
    Announcement Detail
    """
    template_name = 'classroom/homework/pages/studentswork.html'
    model = StudentsWork
    lookup_field = 'pk'
    lookup_url_kwarg = 'work_pk'
    context_object_name ='studentswork'


class StudentsWorkCommentView(HomeWorkMixin, UpdateView):
    """
    Announcement Detail
    """
    template_name = 'classroom/homework/pages/comment.html'
    model = StudentsWork
    lookup_field = 'pk'
    lookup_url_kwarg = 'work_pk'
    context_object_name ='studentswork'
    form_class = StudentWorkCommentForm

    def get_success_url(self):
       """
       for create update and delete view
       """
       return reverse_lazy('classroom:homework:studentswork',
                           kwargs={'slug': self.kwargs['slug'], 'pk':self.kwargs['pk'],
                                   'work_pk':self.kwargs['work_pk']})

