# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import floppyforms.__future__ as forms

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.validators import ValidationError
from django.views.generic import TemplateView, UpdateView, FormView, DeleteView

from extra_views import ModelFormSetView

from braces.views import FormValidMessageMixin

from apps_data.courseevent.models.menu import ClassroomMenuItem
from apps_data.courseevent.models.courseevent import CourseEvent
from apps_data.courseevent.models.forum import Forum
from apps_data.lesson.models.classlesson import ClassLesson

from .mixins.base import CourseMenuMixin, FormCourseEventKwargsMixin


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


class MenuPreView(
    MenuContextPreviewMixin,
    TemplateView):
    """
    Preview of the Classroom menu
    """


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


class MenuItemForm(forms.ModelForm):

    class Meta:
        model = ClassroomMenuItem
        fields = ('display_nr', 'display_title', 'icon', 'item_type',
                  'classlesson', 'forum',
                  'is_start_item', 'is_shortlink')

    def __init__(self, *args, **kwargs):
        courseevent_slug = kwargs.pop('courseevent_slug', None)
        self.courseevent = get_object_or_404(CourseEvent, slug=courseevent_slug)

        super(MenuItemForm, self).__init__(*args, **kwargs)
        self.fields['classlesson'].queryset = \
            ClassLesson.objects.lessons_for_menu(courseevent=self.courseevent)
        self.fields['forum'].queryset = \
            Forum.objects.classroom_menu(courseevent=self.courseevent)


    def clean_display_title(self):
        if self.cleaned_data['display_title'] == "":
            raise ValidationError('''Der Eintrag muss beschriftet werden. ''')
        return self.cleaned_data["display_title"]


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


