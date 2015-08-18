# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import floppyforms.__future__ as forms

from froala_editor.widgets import FroalaEditor

from apps_data.lesson.models.classlesson import ClassLesson


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



