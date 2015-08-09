# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import get_object_or_404

import floppyforms.__future__ as forms

from crispy_forms.helper import FormHelper

from froala_editor.widgets import FroalaEditor

from apps_data.course.models.course import Course
from apps_data.course.models.lesson import Lesson
from apps_data.course.models.material import Material

from mptt.exceptions import InvalidMove
from mptt.forms import TreeNodeChoiceField, TreeNodePositionField

from django.forms.widgets import CheckboxSelectMultiple

class LessonUpdateForm(forms.ModelForm):
    text = forms.CharField(widget=FroalaEditor)

    class Meta:
        model = Lesson
        fields = ('nr', 'title', 'description', 'text', 'material')

    def __init__(self, *args, **kwargs):
        course_slug = kwargs.pop('course_slug', None)
        course = get_object_or_404(Course, slug=course_slug)

        super(LessonUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False

        self.fields["material"].widget = CheckboxSelectMultiple()
        self.fields["material"].queryset = Material.objects.filter(course=course)


class LessonMoveForm(forms.ModelForm):

    class Meta:
        model = Lesson
        fields = ('parent',)

    def __init__(self, *args, **kwargs):
        super(LessonMoveForm, self).__init__(*args, **kwargs)

        self.fields['parent'].queryset = self.instance.possible_parents()
        self.fields['parent'].empty_label=None

        self.helper = FormHelper()
        self.helper.form_tag = False


class LessonCreateForm(forms.ModelForm):

    class Meta:
        model = Lesson
        fields = ('parent', 'nr', 'title', 'description', 'text')

    def __init__(self, *args, **kwargs):
        course_slug = kwargs.pop('course_slug', None)
        course = get_object_or_404(Course, slug=course_slug)
        super(LessonCreateForm, self).__init__(*args, **kwargs)

        self.fields['parent'].queryset = Lesson.parent_choice_new.filter(course=course)
        self.fields['parent'].empty_label=None

        self.helper = FormHelper()
        self.helper.form_tag = False


class LessonAddMaterialForm(forms.ModelForm):

    class Meta:
        model = Lesson
        fields = ('material',)

    def __init__(self, *args, **kwargs):
        super(LessonAddMaterialForm, self).__init__(*args, **kwargs)
        lesson = kwargs['instance']
        self.helper = FormHelper()
        self.helper.form_tag = False
        course = lesson.course

        self.fields['material'].queryset = Material.objects.filter(course=course)