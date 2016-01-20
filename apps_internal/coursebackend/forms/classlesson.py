# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import floppyforms.__future__ as forms

from mptt.forms import TreeNodeChoiceField

from django.shortcuts import get_object_or_404
from django.forms.widgets import CheckboxSelectMultiple

from froala_editor.widgets import FroalaEditor

from apps_data.lesson.models.classlesson import ClassLesson
from apps_data.courseevent.models.courseevent import CourseEvent
from apps_data.material.models.material import Material


class ClassLessonBlockForm(forms.ModelForm):
    text = forms.CharField(widget=FroalaEditor, required=False)

    class Meta:
        model = ClassLesson
        fields = ('nr', 'title', 'description', 'text' )


class ClassLessonForm(forms.ModelForm):
    text = forms.CharField(widget=FroalaEditor, required=False)

    class Meta:
        model = ClassLesson
        fields = ('parent', 'nr', 'title', 'description', 'text' )

    def __init__(self, *args, **kwargs):

        courseevent_slug = kwargs.pop('courseevent_slug', None)
        self.courseevent = get_object_or_404(CourseEvent, slug=courseevent_slug)

        super(ClassLessonForm, self).__init__(*args, **kwargs)

        self.fields['parent'] = TreeNodeChoiceField(
            queryset=ClassLesson.objects.blocks_for_courseevent(courseevent=self.courseevent))
        self.fields['parent'].empty_label = None


class ClassLessonStepForm(forms.ModelForm):
    text = forms.CharField(widget=FroalaEditor, required=False)
    extra_text = forms.CharField(widget=FroalaEditor, required=False)

    class Meta:
        model = ClassLesson
        fields = ('nr',  'title', 'parent', 'description', 'text', 'material', 'is_homework',
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



