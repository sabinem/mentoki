# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, UpdateView, FormView, DeleteView
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.template import loader
from django.forms.models import modelformset_factory
from django.template import Context
from extra_views import FormSetView, ModelFormSetView

from braces.views import FormValidMessageMixin

from apps_data.courseevent.models.menu import ClassroomMenuItem

from apps_data.courseevent.models.courseevent import CourseEvent

from apps_data.lesson.models.classlesson import ClassLesson

from .mixins.base import CourseMenuMixin, FormCourseEventKwargsMixin
from ..forms.menu import MenuItemForm


class MenuSuccessUrlMixin(object):
    """
    sucess url after update, insert or delete of menu item is the preview
    of the classroom menu
    """
    def get_success_url(self):
       return reverse_lazy('coursebackend:menu:preview',
                           kwargs={'slug': self.kwargs['slug'],
                                   'course_slug': self.kwargs['course_slug']})


class MenuContextPreviewMixin(CourseMenuMixin):
    """
    the context in the menu preview are all menuitems for a courseevent
    """
    def get_context_data(self, **kwargs):
        context = super(MenuContextPreviewMixin, self).get_context_data(**kwargs)

        context['classroommenuitems'] = \
            ClassroomMenuItem.objects.all_for_courseevent(courseevent=context['courseevent'])

        return context


class MenuListView(
    CourseMenuMixin,
    TemplateView):
    """
    This views shows the links of menuitem seperated by the item type.
    There are 4 lists so far:
    1. Lessons: Lessons are published by being linked by a menu item
    2. Forums: only level 1 Forums can be menu items
    3. Lessonsteps: Lessonsteps can be published separately, they may
    or may not be part of a published lesson
    """
    def get_context_data(self, **kwargs):
        context = super(MenuListView, self).get_context_data(**kwargs)

        context['lessonitems'] = \
            ClassroomMenuItem.objects.lessons_for_courseevent(
                courseevent=context['courseevent'])
        context['forumitems'] = \
            ClassroomMenuItem.objects.forums_for_courseevent(
                courseevent=context['courseevent'])
        context['homeworkitems'] = \
            ClassroomMenuItem.objects.lessonsteps_for_courseevent(
                courseevent=context['courseevent'])
        context['listitems'] = \
            ClassroomMenuItem.objects.listlinks_for_courseevent(
                courseevent=context['courseevent'])
        return context


class MenuPreView(
    MenuContextPreviewMixin,
    TemplateView):
    """
    Preview of the Classroom menu
    """


class MenuItemUpdateView(
    MenuContextPreviewMixin,
    FormCourseEventKwargsMixin,
    MenuSuccessUrlMixin,
    FormValidMessageMixin,
    UpdateView):
    """
    Classroom Menu Items Update
    """
    model = ClassroomMenuItem
    form_class = MenuItemForm
    context_object_name ='classroomenuitem'
    form_valid_message="Der Eintrag wurde geändert."

    def form_valid(self, form):
        return super(MenuItemUpdateView, self).form_valid(form)

class MenuItemDeleteView(
    CourseMenuMixin,
    MenuSuccessUrlMixin,
    FormValidMessageMixin,
    DeleteView):
    """
    Classroom Menu Item Delete
    """
    model = ClassroomMenuItem
    context_object_name ='classroomenuitem'
    form_valid_message="Der Eintrag wurde gelöscht."


class MenuItemCreateView(
    MenuContextPreviewMixin,
    FormCourseEventKwargsMixin,
    MenuSuccessUrlMixin,
    FormValidMessageMixin,
    FormView):
    """
    Classroom Menu Item Create
    """
    model = ClassroomMenuItem
    form_class = MenuItemForm
    form_valid_message="Der Eintrag wurde gespeichert."

    def form_valid(self, form):
        """
        creates a menu item
        """
        courseevent = get_object_or_404(CourseEvent, slug=self.kwargs['slug'])
        ClassroomMenuItem.objects.create(
            courseevent=courseevent,
            classlesson=form.cleaned_data['classlesson'],
            forum=form.cleaned_data['forum'],
            display_title=form.cleaned_data['display_title'],
            display_nr=form.cleaned_data['display_nr'],
            item_type=form.cleaned_data['item_type'],
            is_start_item=form.cleaned_data['is_start_item'],
            is_shortlink=form.cleaned_data['is_shortlink'],
            icon=form.cleaned_data['icon']
        )

        return HttpResponseRedirect(self.get_success_url())


class MenuUpdateView(
    CourseMenuMixin,
    MenuSuccessUrlMixin,
    ModelFormSetView):
    """
    In this View the whole menu can be updated at once, but only the
    fields display_title and display_nr can be changed here.
    """
    model = ClassroomMenuItem
    fields = ('display_nr', 'display_title')
    extra = 0

    def get_context_data(self, **kwargs):
        """
        all menuitems for the courseevent are fetched
        """
        context = super(MenuUpdateView, self).get_context_data(**kwargs)

        context['classroommenuitems'] = \
            ClassroomMenuItem.objects.all_for_courseevent(
                courseevent=context['courseevent'])

        return context

    def get_queryset(self):
        """
        all menuitems for the courseevent are fetched
        """
        courseevent = get_object_or_404(CourseEvent, slug=self.kwargs['slug'])
        return ClassroomMenuItem.objects.all_for_courseevent(
            courseevent=courseevent)


