# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.core.validators import ValidationError
from django.shortcuts import get_object_or_404
from django.forms.widgets import CheckboxSelectMultiple

import floppyforms.__future__ as forms

from froala_editor.widgets import FroalaEditor

from mptt.forms import TreeNodeChoiceField

from apps_data.course.models.course import Course
from apps_data.courseevent.models.courseevent import CourseEvent
from apps_data.lesson.models.classlesson import ClassLesson
from apps_data.material.models.material import Material


class ClassLessonForm(forms.ModelForm):
    text = forms.CharField(widget=FroalaEditor, required=False)

    class Meta:
        model = ClassLesson
        fields = ('nr', 'title', 'description', 'text' )


class ClassLessonStepForm(forms.ModelForm):
    text = forms.CharField(widget=FroalaEditor, required=False)
    materials = forms.CheckboxSelectMultiple()

    class Meta:
        model = ClassLesson
        fields = ('nr', 'title', 'description', 'text', 'materials' )



