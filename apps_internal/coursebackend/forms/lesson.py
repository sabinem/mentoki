# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import get_object_or_404

import floppyforms.__future__ as forms

from crispy_forms.helper import FormHelper

from apps_data.course.models.course import Course
from apps_data.course.models.lesson import Lesson
from apps_data.course.models.material import Material

from mptt.exceptions import InvalidMove
from mptt.forms import TreeNodeChoiceField, TreeNodePositionField

from django.forms.widgets import CheckboxSelectMultiple

class LessonUpdateForm(forms.ModelForm):

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


class xLessonForm(forms.ModelForm):
    #parent = ModelChoiceField(queryset=Category.objects.all())

    class Meta:
        model = Lesson
        fields = ('nr', 'title', 'description', 'text')

    def __init__(self, *args, **kwargs):

        course_slug = kwargs.pop('course_slug', None)
        pk = kwargs.pop('pk', None)
        course = get_object_or_404(Course, slug=course_slug)

        super(xLessonForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        parent_choices = Lesson.objects.filter(course=course)
        if pk:
            parent_choices.exclude(id=pk)
        self.fields['parent'].queryset = parent_choices
        #category = ModelChoiceField(queryset=Category.objects.all())

    def clean(self):
        cleaned_data = super(xLessonForm, self).clean()
        parent = cleaned_data.get("parent")

        if self.instance:
            add_level = self.instance_level
        if parent.level + self.instance.level > 0:
            # Only do something if both fields are valid so far.
                raise forms.ValidationError(
                    "Abschnitt darf nicht einen Unterabschnitt haben."
                )




class LessonAddMaterialForm(forms.ModelForm):

    class Meta:
        model = Lesson
        fields = ('material',)

    def __init__(self, *args, **kwargs):

        course_slug = kwargs.pop('course_slug', None)
        course = get_object_or_404(Course, slug=course_slug)

        super(LessonAddMaterialForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False

        self.fields['material'].queryset = Material.objects.filter(course=course)