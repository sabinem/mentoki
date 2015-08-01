# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponseRedirect

from vanilla import TemplateView, DetailView, UpdateView, FormView, DeleteView

from apps_data.courseevent.models.homework import Homework
from apps_data.courseevent.models.courseevent import CourseEvent

from .mixins.base import CourseMenuMixin
from ..forms.homework import HomeworkForm


class HomeworkMixin(CourseMenuMixin):

    def get_success_url(self):
       """
       for create update and delete view
       """
       return reverse_lazy('classroom:studentswork:list',
                           kwargs={'slug': self.kwargs['slug']})


class HomeworkStartView(HomeworkMixin, TemplateView):
    """
    Work List
    """
    template_name = 'classroom/studentswork/pages/list.html'

    def get_context_data(self, **kwargs):
        context = super(HomeworkStartView, self).get_context_data(**kwargs)

        context['studentworks'] = Homework.objects.mywork(user=self.request.user,
                                                              courseevent=context['courseevent'])
        return context


class HomeworkDetailView(HomeworkMixin, DetailView):
    """
    Work Detail
    """
    template_name = 'classroom/studentswork/pages/detail.html'
    model = Homework
    lookup_field = 'pk'
    context_object_name ='work'


class HomeworkUpdateView(HomeworkMixin, UpdateView):
    """
    Work Update
    """
    template_name = 'classroom/studentswork/pages/update.html'
    model = Homework
    form_class = HomeworkForm
    lookup_field = 'pk'
    context_object_name ='work'


class HomeworkDeleteView(HomeworkMixin, DeleteView):
    """
    Work Delete
    """
    template_name = 'classroom/studentswork/pages/delete.html'
    model = Homework
    lookup_field = 'pk'
    context_object_name ='work'


class HomeworkCreateView(HomeworkMixin, FormView):
    """
    Work Create
    """
    template_name = 'classroom/studentswork/pages/create.html'
    model = HomeworkMixin
    lookup_field = 'pk'
    form_class = HomeworkForm
    context_object_name ='work'

    def form_valid(self, form):
        courseevent = get_object_or_404(CourseEvent, slug=self.kwargs['slug'])
        Homework.objects.create_new_work(
            courseevent=courseevent,
            homework=form.cleaned_data['homework'],
            text=form.cleaned_data['text'],
            title=form.cleaned_data['title'],
            user=self.request.user)

        return HttpResponseRedirect(self.get_success_url())



