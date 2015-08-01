# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import floppyforms.__future__ as forms

from froala_editor.widgets import FroalaEditor

from apps_data.courseevent.models.homework import StudentsWork


class StudentWorkForm(forms.ModelForm):
    text = forms.CharField(widget=FroalaEditor)

    class Meta:
        model = StudentsWork
        fields = ('homework', 'title', 'text', 'published')


class StudentWorkAddTeamForm(forms.ModelForm):

    class Meta:
        model = StudentsWork
        fields = ('workers',)
        widgets = {'workers': forms.CheckboxSelectMultiple}

    def __init__(self, *args, **kwargs):
        super(StudentWorkAddTeamForm, self).__init__(*args, **kwargs)
        work = kwargs['instance']
        self.fields['workers'].queryset = work.courseevent.students()


class StudentWorkCommentForm(forms.ModelForm):
    comments = forms.CharField(widget=FroalaEditor)

    class Meta:
        model = StudentsWork
        fields = ('comments',)
