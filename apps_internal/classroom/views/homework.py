# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import get_object_or_404

from vanilla import TemplateView, DetailView

from apps_data.courseevent.models.homework import Homework, StudentsWork

from .mixins.base import ClassroomMenuMixin


class HomeWorkListView(ClassroomMenuMixin, TemplateView):
    """
    AnnouncementList
    """
    template_name = 'classroom/homework/list.html'

    def get_context_data(self, **kwargs):
        context = super(HomeWorkListView, self).get_context_data(**kwargs)

        context['homework'] = get_object_or_404(Homework, pk=self.kwargs['pk'])

        context['studentsworks'] = \
            StudentsWork.objects.turnedin_homework(homework=context['homework'])

        print context['studentsworks']

        return context


class HomeWorkDetailView(ClassroomMenuMixin, TemplateView):
    """
    Announcement Detail
    """
    template_name = 'classroom/homework/detail.html'
    model = StudentsWork
    lookup_field = 'pk'
    context_object_name ='work'