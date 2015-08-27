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

from .mixins.base import CourseMenuMixin, FormCourseEventKwargsMixin
from ..forms.menu import MenuItemForm


class MenuSuccessUrlMixin(object):
    def get_success_url(self):
       return reverse_lazy('coursebackend:menu:preview',
                           kwargs={'slug': self.kwargs['slug'],
                                   'course_slug': self.kwargs['course_slug']})


class MenuContextPreviewMixin(CourseMenuMixin):
    def get_context_data(self, **kwargs):
        context = super(MenuContextPreviewMixin, self).get_context_data(**kwargs)

        context['classroommenuitems'] = \
            ClassroomMenuItem.objects.all_for_courseevent(courseevent=context['courseevent'])

        return context


class MenuListView(
    CourseMenuMixin,
    TemplateView):
    """
    Classroom Menu Items List
    """
    def get_context_data(self, **kwargs):
        context = super(MenuListView, self).get_context_data(**kwargs)

        context['lessonitems'] = \
            ClassroomMenuItem.objects.lessons_for_courseevent(courseevent=context['courseevent'])
        context['homeworkitems'] = \
            ClassroomMenuItem.objects.homeworks_for_courseevent(courseevent=context['courseevent'])
        context['forumitems'] = \
            ClassroomMenuItem.objects.forums_for_courseevent(courseevent=context['courseevent'])
        context['listitems'] = \
            ClassroomMenuItem.objects.listlinks_for_courseevent(courseevent=context['courseevent'])
        return context


class MenuPreView(
    MenuContextPreviewMixin,
    TemplateView):
    """
    Classroom Menu Items List
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
        courseevent = get_object_or_404(CourseEvent, slug=self.kwargs['slug'])
        ClassroomMenuItem.objects.create(
            courseevent=courseevent,
            homework=form.cleaned_data['homework'],
            classlesson=form.cleaned_data['classlesson'],
            forum=form.cleaned_data['forum'],
            display_title=form.cleaned_data['display_title'],
            display_nr=form.cleaned_data['display_nr'],
            item_type=form.cleaned_data['item_type'],
            is_start_item=form.cleaned_data['is_start_item'],
            is_shortlink=form.cleaned_data['is_shortlink']
        )

        return HttpResponseRedirect(self.get_success_url())


class MenuUpdateView(
    CourseMenuMixin,
    MenuSuccessUrlMixin,
    ModelFormSetView):
    """
    Classroom Menu Items List Update
    """
    model = ClassroomMenuItem
    fields = ('display_nr', 'display_title')
    extra = 0

    def get_context_data(self, **kwargs):
        context = super(MenuUpdateView, self).get_context_data(**kwargs)

        context['classroommenuitems'] = \
            ClassroomMenuItem.objects.all_for_courseevent(courseevent=context['courseevent'])

        return context

    def get_queryset(self):
        courseevent = get_object_or_404(CourseEvent, slug=self.kwargs['slug'])
        return ClassroomMenuItem.objects.all_for_courseevent(courseevent=courseevent)


