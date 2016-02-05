# coding: utf-8

from __future__ import unicode_literals, absolute_import

import floppyforms.__future__ as forms

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import UpdateView, \
    FormView

from braces.views import FormValidMessageMixin

from froala_editor.widgets import FroalaEditor

from apps_data.lesson.models.classlesson import ClassLesson

from apps_data.courseevent.models.courseevent import CourseEvent

from ..mixins.base import CourseMenuMixin
from .mixin import ClassLessonBreadcrumbMixin, ClassLessonSuccessUpdateUrlMixin

import logging
logger = logging.getLogger(__name__)


class ClassLessonBlockForm(forms.ModelForm):
    text = forms.CharField(widget=FroalaEditor, required=False)

    class Meta:
        model = ClassLesson
        fields = ('nr', 'title', 'description', 'text' )


class ClassLessonBlockUpdateView(
    CourseMenuMixin,
    ClassLessonBreadcrumbMixin,
    FormValidMessageMixin,
    ClassLessonSuccessUpdateUrlMixin,
    UpdateView):
    """
    Update a classlesson step
    """
    model = ClassLesson
    context_object_name = 'classlessonblock'
    form_class = ClassLessonBlockForm
    form_valid_message = "Der Unterrichtsblock wurde geändert!"



class ClassLessonBlockCreateView(
    CourseMenuMixin,
    FormValidMessageMixin,
    FormView):
    """
    create lesson
    """
    form_class = ClassLessonBlockForm
    model = ClassLesson
    context_object_name ='classlessonblock'
    form_valid_message = "Der Block wurde angelegt!"

    def form_valid(self, form):

        courseevent = get_object_or_404(CourseEvent, slug=self.kwargs['slug'])
        self.object = ClassLesson.objects.create_classlessonblock(
            courseevent=courseevent,
            title=form.cleaned_data['title'],
            description=form.cleaned_data['description'],
            text=form.cleaned_data['text'],
            nr=form.cleaned_data['nr']
        )
        last_url = self.request.session['last_url']
        return HttpResponseRedirect(last_url)

