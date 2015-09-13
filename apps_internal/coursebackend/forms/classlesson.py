# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import floppyforms.__future__ as forms

from django.shortcuts import get_object_or_404
from django.forms.widgets import CheckboxSelectMultiple

from froala_editor.widgets import FroalaEditor

from apps_data.lesson.models.classlesson import ClassLesson
from apps_data.course.models.course import Course
from apps_data.material.models.material import Material


class ClassLessonForm(forms.ModelForm):
    text = forms.CharField(widget=FroalaEditor, required=False)

    class Meta:
        model = ClassLesson
        fields = ('nr', 'title', 'description', 'text' )


class ClassLessonHomeworkForm(forms.ModelForm):
    text = forms.CharField(widget=FroalaEditor, required=False)
    extra_text = forms.CharField(widget=FroalaEditor, required=False)

    class Meta:
        model = ClassLesson
        fields = ('nr', 'title', 'description', 'text', 'material', 'due_date', 'extra_text' )

    def __init__(self, *args, **kwargs):
        course_slug = kwargs.pop('course_slug', None)
        self.course = get_object_or_404(Course, slug=course_slug)

        super(ClassLessonHomeworkForm, self).__init__(*args, **kwargs)

        self.fields['material'].queryset = Material.objects.filter(course=self.course)


class ClassLessonStepForm(forms.ModelForm):
    text = forms.CharField(widget=FroalaEditor, required=False)

    class Meta:
        model = ClassLesson
        fields = ('nr', 'title', 'description', 'text', 'material', 'is_homework' )

    def __init__(self, *args, **kwargs):
        course_slug = kwargs.pop('course_slug', None)
        self.course = get_object_or_404(Course, slug=course_slug)

        super(ClassLessonStepForm, self).__init__(*args, **kwargs)

        self.fields['material'].queryset = Material.objects.filter(course=self.course)