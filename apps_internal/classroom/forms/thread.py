# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import floppyforms.__future__ as forms

from froala_editor.widgets import FroalaEditor

from apps_data.courseevent.models.forum import Thread


class StudentThreadForm(forms.ModelForm):
    text = forms.CharField(widget=FroalaEditor)

    class Meta:
        model = Thread
        fields = ('title', 'text')

    def __init__(self, *args, **kwargs):
        super(StudentThreadForm, self).__init__(*args, **kwargs)