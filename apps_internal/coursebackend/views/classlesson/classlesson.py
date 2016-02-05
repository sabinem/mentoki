# coding: utf-8

from __future__ import unicode_literals, absolute_import
import floppyforms.__future__ as forms

from django.http import HttpResponseRedirect
from django.views.generic import UpdateView, \
    FormView
from django.shortcuts import get_object_or_404

from mptt.forms import TreeNodeChoiceField

from froala_editor.widgets import FroalaEditor

from braces.views import FormValidMessageMixin

from apps_data.lesson.models.lesson import Lesson
from apps_data.lesson.models.classlesson import ClassLesson
from apps_data.courseevent.models.courseevent import CourseEvent

from ..mixins.base import CourseMenuMixin, FormCourseEventKwargsMixin
from .mixin import ClassLessonBreadcrumbMixin, ClassLessonSuccessUpdateUrlMixin

import logging
logger = logging.getLogger(__name__)


class ClassLessonForm(forms.ModelForm):
    text = forms.CharField(widget=FroalaEditor, required=False)

    class Meta:
        model = ClassLesson
        fields = ('parent', 'nr', 'show_number', 'title', 'description', 'text' )

    def __init__(self, *args, **kwargs):

        courseevent_slug = kwargs.pop('courseevent_slug', None)
        self.courseevent = get_object_or_404(CourseEvent, slug=courseevent_slug)

        super(ClassLessonForm, self).__init__(*args, **kwargs)

        self.fields['parent'] = TreeNodeChoiceField(
            queryset=ClassLesson.objects.blocks_for_courseevent(courseevent=self.courseevent))
        self.fields['parent'].empty_label = None


class ClassLessonUpdateView(
    CourseMenuMixin,
    ClassLessonBreadcrumbMixin,
    FormValidMessageMixin,
    FormCourseEventKwargsMixin,
    ClassLessonSuccessUpdateUrlMixin,
    UpdateView):
    """
    Update a classlesson
    """
    form_class = ClassLessonForm
    model = ClassLesson
    context_object_name = 'classlesson'
    form_valid_message = "Die Lektion wurde geändert!"


class ClassLessonCreateView(
    CourseMenuMixin,
    FormCourseEventKwargsMixin,
    ClassLessonSuccessUpdateUrlMixin,
    FormValidMessageMixin,
    FormView):
    """
    create lesson
    """
    form_class = ClassLessonForm
    model = Lesson
    context_object_name ='classlesson'
    form_valid_message = "Die Lektion wurde angelegt!"

    def form_valid(self, form):
        courseevent = get_object_or_404(CourseEvent, slug=self.kwargs['slug'])
        self.object = ClassLesson.objects.create_classlesson(
            courseevent=courseevent,
            title=form.cleaned_data['title'],
            description=form.cleaned_data['description'],
            text=form.cleaned_data['text'],
            parent=form.cleaned_data['parent'],
            nr=form.cleaned_data['nr'],
            show_number = form.cleaned_data['show_number'],
        )
        last_url = self.request.session['last_url']
        return HttpResponseRedirect(last_url)

