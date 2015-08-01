# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponseRedirect

from vanilla import TemplateView, DetailView, UpdateView, FormView, DeleteView

from apps_data.courseevent.models.homework import StudentsWork
from apps_data.courseevent.models.courseevent import CourseEvent

from .mixins.base import ClassroomMenuMixin
from ..forms.studentswork import StudentWorkForm, StudentWorkAddTeamForm


class StudentsWorkChangeMixin(ClassroomMenuMixin):

    def get_success_url(self):
       """
       for create update and delete view
       """
       return reverse_lazy('classroom:studentswork:list',
                           kwargs={'slug': self.kwargs['slug']})


class StudentsWorkListView(ClassroomMenuMixin, TemplateView):
    """
    Work: List
    """
    def get_context_data(self, **kwargs):
        context = super(StudentsWorkListView, self).get_context_data(**kwargs)

        context['studentsworks'] = StudentsWork.objects.mywork(user=self.request.user,
                                                              courseevent=context['courseevent'])
        return context


class StudentsWorkDetailView(ClassroomMenuMixin, DetailView):
    """
    Work: Detail
    """
    model = StudentsWork
    lookup_field = 'pk'
    context_object_name ='studentswork'


class StudentsWorkUpdateView(StudentsWorkChangeMixin, UpdateView):
    """
    Work: Update
    """
    model = StudentsWork
    form_class = StudentWorkForm
    lookup_field = 'pk'
    context_object_name ='studentswork'


class StudentsWorkDeleteView(StudentsWorkChangeMixin, DeleteView):
    """
    Work: Delete
    """
    model = StudentsWork
    lookup_field = 'pk'
    context_object_name ='studentswork'


class StudentsWorkCreateView(StudentsWorkChangeMixin, FormView):
    """
    Work: Create
    """
    model = StudentsWork
    lookup_field = 'pk'
    form_class = StudentWorkForm
    context_object_name ='studentswork'

    def form_valid(self, form):
        courseevent = get_object_or_404(CourseEvent, slug=self.kwargs['slug'])
        StudentsWork.objects.create_new_work(
            courseevent=courseevent,
            homework=form.cleaned_data['homework'],
            text=form.cleaned_data['text'],
            title=form.cleaned_data['title'],
            user=self.request.user)

        return HttpResponseRedirect(self.get_success_url())


class StudentsWorkAddTeamView(StudentsWorkChangeMixin, UpdateView):
    """
    Work: Add Team Members
    """
    model = StudentsWork
    lookup_field = 'pk'
    form_class = StudentWorkAddTeamForm
    context_object_name = 'studentswork'

