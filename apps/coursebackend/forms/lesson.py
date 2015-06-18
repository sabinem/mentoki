# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import get_object_or_404

import floppyforms.__future__ as forms

from crispy_forms.helper import FormHelper

from apps.course.models import Lesson, Course, Material


class LessonForm(forms.ModelForm):

    class Meta:
        model = Lesson
        fields = ('parent','nr', 'title', 'description', 'text')

    def __init__(self, *args, **kwargs):

        course_slug = kwargs.pop('course_slug', None)
        course = get_object_or_404(Course, slug=course_slug)

        super(LessonForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.fields['parent'].queryset = Lesson.objects.filter(course=course)


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