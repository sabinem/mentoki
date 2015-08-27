# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import floppyforms.__future__ as forms

from froala_editor.widgets import FroalaEditor

from apps_data.courseevent.models.homework import StudentsWork, Comment

class StudentWorkCreateForm(forms.ModelForm):
    text = forms.CharField(widget=FroalaEditor)

    class Meta:
        model = StudentsWork
        fields = ('homework', 'title', 'text' )


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
        super(StudentWorkAddTeamForm, self).__init__(*args, **kwargs)
        studentswork = kwargs['instance']
        self.fields['workers'].queryset = studentswork.courseevent.students()


class StudentWorkCommentForm(forms.ModelForm):
    text = forms.CharField(widget=FroalaEditor)

    class Meta:
        model = Comment
        fields = ('title', 'text')
