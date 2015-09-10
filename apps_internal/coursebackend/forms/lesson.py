# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import get_object_or_404
from django.forms.widgets import CheckboxSelectMultiple

import floppyforms.__future__ as forms

from froala_editor.widgets import FroalaEditor

from mptt.forms import TreeNodeChoiceField

from apps_data.course.models.course import Course
from apps_data.lesson.models.lesson import Lesson
from apps_data.material.models.material import Material


class LessonBlockForm(forms.ModelForm):
    text = forms.CharField(widget=FroalaEditor)

    class Meta:
        model = Lesson
        fields = ('title', 'description', 'text', 'block_sort')

    def __init__(self, *args, **kwargs):
        super(LessonBlockForm, self).__init__(*args, **kwargs)
        self.fields['text'].required = False


class LessonForm(forms.ModelForm):
    text = forms.CharField(widget=FroalaEditor, required=False)

    class Meta:
        model = Lesson
        fields = ('parent', 'nr', 'title', 'description', 'text' )

    def __init__(self, *args, **kwargs):
        course_slug = kwargs.pop('course_slug', None)
        self.course = get_object_or_404(Course, slug=course_slug)

        super(LessonForm, self).__init__(*args, **kwargs)

        self.fields['parent'].empty_label = None
        self.fields["parent"].queryset = \
            Lesson.objects.blocks_for_course(course=self.course)


class LessonStepForm(forms.ModelForm):
    text = forms.CharField(widget=FroalaEditor, required=False)

    class Meta:
        model = Lesson
        fields = ('parent', 'nr', 'title', 'description', 'text', 'material', 'is_homework' )

    def __init__(self, *args, **kwargs):
        course_slug = kwargs.pop('course_slug', None)
        self.course = get_object_or_404(Course, slug=course_slug)

        super(LessonStepForm, self).__init__(*args, **kwargs)

        self.fields['parent'].empty_label = None
        self.fields['parent'] = TreeNodeChoiceField(
            queryset=Lesson.objects.lessons_for_course(course=self.course),
            level_indicator=u'+--')
        self.fields['material'].queryset = Material.objects.materials_for_course(course=self.course)


