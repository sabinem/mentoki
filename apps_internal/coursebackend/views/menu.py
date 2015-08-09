# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.forms.formsets import formset_factory

from django.views.generic import TemplateView, UpdateView, FormView, DeleteView

from extra_views import ModelFormSetView

from apps_data.courseevent.models.menu import ClassroomMenuItem

from apps_data.courseevent.models.courseevent import CourseEvent

from .mixins.base import CourseMenuMixin
from ..forms.menu import MenuItemForm


class ClassroomMenuMixin(CourseMenuMixin):

    def get_success_url(self):
       """
       for create update and delete view
       """
       return reverse_lazy('coursebackend:menu:list',
                           kwargs={'slug': self.kwargs['slug'],
                                   'course_slug': self.kwargs['course_slug']})


class MenuListView(CourseMenuMixin, TemplateView):
    """
    Classroom Menu Items List
    """
    def get_context_data(self, **kwargs):
        context = super(MenuListView, self).get_context_data(**kwargs)

        context['classroommenuitems'] = \
            ClassroomMenuItem.objects.all_for_courseevent(courseevent=context['courseevent'])

        return context


class MenuPreView(CourseMenuMixin, TemplateView):
    """
    Classroom Menu Items List
    """
    def get_context_data(self, **kwargs):
        context = super(MenuPreView, self).get_context_data(**kwargs)

        context['classroommenuitems'] = \
            ClassroomMenuItem.objects.all_for_courseevent(courseevent=context['courseevent'])

        return context


class MenuItemUpdateView(ClassroomMenuMixin, UpdateView):
    """
    Classroom Menu Items Update
    """
    model = ClassroomMenuItem
    form_class = MenuItemForm
    context_object_name ='classroomenuitem'

    def get_form_kwargs(self):
        course_slug = self.kwargs['course_slug']
        courseevent_slug = self.kwargs['slug']
        kwargs = super(MenuItemUpdateView, self).get_form_kwargs()
        kwargs['course_slug']=course_slug
        kwargs['courseevent_slug']=courseevent_slug
        return kwargs


class MenuUpdateView(CourseMenuMixin, ModelFormSetView):
    """
    Classroom Menu Items List Update
    """
    model = ClassroomMenuItem
    fields = ('display_nr', 'display_title', 'item_type' )
    readonly = ('link',)
    can_order = True

    #def get_queryset(self):
    #    slug = self.kwargs['slug']
    #    return super(MenuUpdateView, self).get_queryset().filter(slug=slug)

    def get_context_data(self, **kwargs):
        context = super(MenuUpdateView, self).get_context_data(**kwargs)
        print "============================="
        print context
        print "-----"
        print context['formset']

        return context

class MenuItemDeleteView(CourseMenuMixin, DeleteView):
    """
    Classroom Menu Item Delete
    """
    model = ClassroomMenuItem
    lookup_field = 'pk'
    context_object_name ='classroomenuitem'


class MenuItemCreateView(ClassroomMenuMixin, FormView):
    """
    Classroom Menu Item Create
    """
    model = ClassroomMenuItem
    form_class = MenuItemForm

    def get_context_data(self, **kwargs):
        context = super(MenuItemCreateView, self).get_context_data(**kwargs)

        context['classroommenuitems'] = \
            ClassroomMenuItem.objects.all_for_courseevent(courseevent=context['courseevent'])

        return context


    def get_form_kwargs(self):
        course_slug = self.kwargs['course_slug']
        courseevent_slug = self.kwargs['slug']
        kwargs = super(MenuItemCreateView, self).get_form_kwargs()
        kwargs['course_slug']=course_slug
        kwargs['courseevent_slug']=courseevent_slug
        return kwargs

    def form_valid(self, form):
        courseevent = get_object_or_404(CourseEvent, slug=self.kwargs['slug'])
        ClassroomMenuItem.objects.create(
            courseevent=courseevent,
            homework=form.cleaned_data['homework'],
            lesson=form.cleaned_data['lesson'],
            forum=form.cleaned_data['forum'],
            display_title=form.cleaned_data['display_title'],
            display_nr=form.cleaned_data['display_nr'],
            published=form.cleaned_data['published'],
            item_type=form.cleaned_data['item_type'],
            is_start_item=form.cleaned_data['is_start_item']
        )

        return HttpResponseRedirect(self.get_success_url())



