# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponseRedirect

from vanilla import TemplateView, DetailView, UpdateView, FormView, DeleteView

from apps_data.courseevent.models.menu import ClassroomMenuItem
from apps_data.courseevent.models.courseevent import CourseEvent

from .mixins.base import CourseMenuMixin
from ..forms.menu import MenuForm


class ClassroomMenuMixin(CourseMenuMixin):

    def get_success_url(self):
       """
       for create update and delete view
       """
       return reverse_lazy('classroom:studentswork:list',
                           kwargs={'slug': self.kwargs['slug']})


class MenuStartView(CourseMenuMixin, TemplateView):
    """
    Work List
    """
    template_name = 'classroom/studentswork/pages/list.html'

    def get_context_data(self, **kwargs):
        context = super(MenuStartView, self).get_context_data(**kwargs)

        context['studentworks'] = ClassroomMenuItem.objects.mywork(user=self.request.user,
                                                              courseevent=context['courseevent'])
        return context


class StudentsWorkDetailView(ClassroomMenuMixin, DetailView):
    """
    Work Detail
    """
    template_name = 'classroom/studentswork/pages/detail.html'
    model = ClassroomMenuItem
    lookup_field = 'pk'
    context_object_name ='work'


class StudentsWorkUpdateView(CourseMenuMixin, UpdateView):
    """
    Work Update
    """
    template_name = 'classroom/studentswork/pages/update.html'
    model = ClassroomMenuItem
    form_class = MenuForm
    lookup_field = 'pk'
    context_object_name ='work'


class StudentsWorkDeleteView(CourseMenuMixin, DeleteView):
    """
    Work Delete
    """
    template_name = 'classroom/studentswork/pages/delete.html'
    model = ClassroomMenuItem
    lookup_field = 'pk'
    context_object_name ='work'


class StudentsWorkCreateView(CourseMenuMixin, FormView):
    """
    Work Create
    """
    template_name = 'classroom/studentswork/pages/create.html'
    model = ClassroomMenuItem
    lookup_field = 'pk'
    form_class = MenuForm
    context_object_name ='work'

    def form_valid(self, form):
        courseevent = get_object_or_404(CourseEvent, slug=self.kwargs['slug'])
        ClassroomMenuItem.objects.create_new_work(
            courseevent=courseevent,
            homework=form.cleaned_data['homework'],
            text=form.cleaned_data['text'],
            title=form.cleaned_data['title'],
            user=self.request.user)

        return HttpResponseRedirect(self.get_success_url())



