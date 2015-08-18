# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import get_object_or_404

import floppyforms.__future__ as forms

from froala_editor.widgets import FroalaEditor

from apps_data.lesson.models.classlesson import ClassLesson
from apps_data.courseevent.models.homework import Homework
from apps_data.courseevent.models.courseevent import CourseEvent


class HomeworkForm(forms.ModelForm):
    text = forms.CharField(widget=FroalaEditor)

    class Meta:
        model = Homework
        fields = ('title', 'text', 'classlesson', 'due_date')

    def __init__(self, *args, **kwargs):
        courseevent_slug = kwargs.pop('courseevent_slug', None)
        self.courseevent = get_object_or_404(CourseEvent, slug=courseevent_slug)

        super(HomeworkForm, self).__init__(*args, **kwargs)

        self.fields["classlesson"].queryset = \
            ClassLesson.objects.lessons_for_courseevent(courseevent=self.courseevent)