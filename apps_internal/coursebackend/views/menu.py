# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.forms.formsets import formset_factory

from vanilla import TemplateView, DetailView, UpdateView, FormView, DeleteView

from apps_data.courseevent.models.menu import ClassroomMenuItem
from apps_data.courseevent.models.courseevent import CourseEvent

from .mixins.base import CourseMenuMixin
from ..forms.menu import MenuItemForm


class ClassroomMenuMixin(CourseMenuMixin):

    def get_success_url(self):
       """
       for create update and delete view
       """
       return reverse_lazy('coursebackend:classroommenuitem:list',
                           kwargs={'slug': self.kwargs['slug']})


class MenuListView(CourseMenuMixin, TemplateView):
    """
    Classroom Menu Items List
    """
    def get_context_data(self, **kwargs):
        context = super(MenuListView, self).get_context_data(**kwargs)

        context['classroommenuitems'] = \
            ClassroomMenuItem.objects.all_for_courseevent(courseevent=context['courseevent'])

        return context


class MenuUpdateView(CourseMenuMixin, FormView):
    """
    Classroom Menu Items List Update
    """
    model = ClassroomMenuItem
    form_class = MenuItemForm

    def get(self, request, *args, **kwargs):
        pass


class MenuItemUpdateView(CourseMenuMixin, FormView):
    """
    Classroom Menu Items List Update
    """
    model = ClassroomMenuItem
    form_class = MenuItemForm

    def get(self, request, *args, **kwargs):
        pass


class MenuItemDeleteView(CourseMenuMixin, DeleteView):
    """
    Classroom Menu Item Delete
    """
    model = ClassroomMenuItem
    lookup_field = 'pk'
    context_object_name ='classroomenuitem'


class MenuItemCreateView(CourseMenuMixin, FormView):
    """
    Classroom Menu Item Create
    """
    model = ClassroomMenuItem
    lookup_field = 'pk'
    form_class = MenuItemForm
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



