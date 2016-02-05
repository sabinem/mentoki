# coding: utf-8

from __future__ import unicode_literals, absolute_import

import floppyforms.__future__ as forms

from mptt.forms import TreeNodeChoiceField

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import UpdateView, \
    FormView

from braces.views import FormValidMessageMixin

from froala_editor.widgets import FroalaEditor

from apps_data.lesson.models.classlesson import ClassLesson
from apps_data.material.models.material import Material
from apps_data.lesson.models.lesson import Lesson
from apps_data.courseevent.models.courseevent import CourseEvent

from ..mixins.base import CourseMenuMixin, FormCourseEventKwargsMixin, FormCourseKwargsMixin
from .mixin import ClassLessonBreadcrumbMixin, ClassLessonSuccessUpdateUrlMixin

import logging
logger = logging.getLogger(__name__)


class ClassLessonStepForm(forms.ModelForm):
    text = forms.CharField(widget=FroalaEditor, required=False)
    extra_text = forms.CharField(widget=FroalaEditor, required=False)

    class Meta:
        model = ClassLesson
        fields = ('nr',  'title', 'parent', 'description','show_number', 'text', 'material', 'is_homework',
                  'show_work_area', 'due_date', 'extra_text' )

    def __init__(self, *args, **kwargs):
        courseevent_slug = kwargs.pop('courseevent_slug', None)
        self.courseevent = get_object_or_404(CourseEvent, slug=courseevent_slug)

        super(ClassLessonStepForm, self).__init__(*args, **kwargs)

        self.fields['material'].queryset = \
            Material.objects.materials_for_course(course=self.courseevent.course)

        self.fields['parent'] = TreeNodeChoiceField(
            queryset=ClassLesson.objects.lessons_for_courseevent(courseevent=self.courseevent))
        self.fields['parent'].empty_label = None


class ClassLessonStepUpdateView(
    CourseMenuMixin,
    ClassLessonBreadcrumbMixin,
    FormValidMessageMixin,
    FormCourseEventKwargsMixin,
    ClassLessonSuccessUpdateUrlMixin,
    UpdateView):
    """
    Update a classlesson step
    """
    model = ClassLesson
    context_object_name = 'classlessonstep'
    form_class = ClassLessonStepForm
    form_valid_message = "Der Lernabschnitt wurde geändert!"


class ClassLessonStepCreateView(
    CourseMenuMixin,
    FormCourseEventKwargsMixin,
    ClassLessonSuccessUpdateUrlMixin,
    FormValidMessageMixin,
    FormView):
    """
    create lesson step, special: add materials if requested
    """
    form_class = ClassLessonStepForm
    model = Lesson
    context_object_name ='lessonstep'
    form_valid_message = "Der Lernabschnitt wurde angelegt!"

    def form_valid(self, form):
        courseevent = get_object_or_404(CourseEvent, slug=self.kwargs['course_slug'])

        self.object = ClassLesson.objects.create_classstep(
            courseevent=courseevent,
            title=form.cleaned_data['title'],
            description=form.cleaned_data['description'],
            text=form.cleaned_data['text'],
            material=form.cleaned_data['material'],
            nr=form.cleaned_data['nr'],
            parent=form.cleaned_data['parent'],
            is_homework = form.cleaned_data['is_homework'],
            show_number = form.cleaned_data['show_number'],
        )
        last_url = self.request.session['last_url']
        return HttpResponseRedirect(last_url)
