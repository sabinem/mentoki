# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.core.validators import ValidationError
from django.shortcuts import get_object_or_404
from django.forms.widgets import CheckboxSelectMultiple

import floppyforms.__future__ as forms

from apps_data.lesson.models.lesson import Lesson


class LessonCopyForm(forms.Form):
    copy_lessonsteps = forms.ModelMultipleChoiceField(
        queryset=None,
        widget=CheckboxSelectMultiple,
        required=False
    )
    copy_lesson = forms.BooleanField(
        required=False
    )

    def __init__(self, *args, **kwargs):
        lesson_pk = kwargs.pop('lesson_pk', None)
        self.lesson = get_object_or_404(Lesson, pk=lesson_pk)

        super(LessonCopyForm, self).__init__(*args, **kwargs)
        self.fields['copy_lessonsteps'].queryset = self.lesson.get_children()

    def clean(self):
        if self.cleaned_data['copy_lesson']:
            if self.cleaned_data['copy_lessonsteps']:

                raise ValidationError('''Wenn die Lektion erneuert wird,
                werden auch alle Unterlektionen neu geholt: Also entweder Lektion
                oder Unterlektionen auswählen!''')
        else:
            if self.cleaned_data['copy_lessonsteps'] == []:
                raise ValidationError('''Es wurde nichts ausgewählt! Bitte etwas auswählen!''')









