# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import floppyforms.__future__ as forms

from django.shortcuts import get_object_or_404
from mentoki.settings import AUTH_USER_MODEL

from froala_editor.widgets import FroalaEditor

from apps_data.courseevent.models.courseevent import CourseEvent
from apps_data.courseevent.models.homework import StudentsWork, Comment
from apps_data.lesson.models.classlesson import ClassLesson

class StudentWorkCreateForm(forms.ModelForm):
    text = forms.CharField(widget=FroalaEditor)

    class Meta:
        model = StudentsWork
        fields = ('homework', 'title', 'text' )

    def __init__(self, *args, **kwargs):
        courseevent_slug = kwargs.pop('courseevent_slug', None)
        self.courseevent = get_object_or_404(CourseEvent, slug=courseevent_slug)

        super(StudentWorkCreateForm, self).__init__(*args, **kwargs)

        self.fields["homework"].queryset = \
            ClassLesson.objects.published_homeworks(courseevent=self.courseevent)
        self.fields['homework'].empty_label = None


class StudentWorkUpdateForm(forms.ModelForm):
    text = forms.CharField(widget=FroalaEditor)

    class Meta:
        model = StudentsWork
        fields = ('title', 'text', 'published')


class StudentWorkAddTeamForm(forms.ModelForm):

    class Meta:
        model = StudentsWork
        fields = ('workers',)
        widgets = {'workers': forms.CheckboxSelectMultiple}

    def __init__(self, *args, **kwargs):
        courseevent_slug = kwargs.pop('courseevent_slug', None)
        self.courseevent = get_object_or_404(CourseEvent, slug=courseevent_slug)
        super(StudentWorkAddTeamForm, self).__init__(*args, **kwargs)
        studentswork = kwargs['instance']
        self.fields['workers'].queryset = self.courseevent.workers()


class StudentWorkCommentForm(forms.ModelForm):
    text = forms.CharField(widget=FroalaEditor)

    class Meta:
        model = Comment
        fields = ('title', 'text')
