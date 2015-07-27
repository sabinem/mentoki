# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from vanilla import TemplateView, DetailView

from apps_data.courseevent.models.homework import StudentsWork

from .mixins.base import ClassroomMenuMixin


class StudentsWorkListView(ClassroomMenuMixin, TemplateView):
    """
    Work List
    """
    template_name = 'classroom/studentswork/list.html'

    def get_context_data(self, **kwargs):
        context = super(StudentsWorkListView, self).get_context_data(**kwargs)

        context['studentworks'] = StudentsWork.objects.mywork(user=self.request.user,
                                                              courseevent=context['courseevent'])

        return context


class StudentsWorkDetailView(ClassroomMenuMixin, TemplateView):
    """
    Work Detail
    """
    template_name = 'classroom/studentswork/detail.html'
    model = StudentsWork
    lookup_field = 'pk'
    context_object_name ='work'