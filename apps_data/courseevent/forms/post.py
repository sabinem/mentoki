# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import floppyforms.__future__ as forms
from crispy_forms.helper import FormHelper
from froala_editor.widgets import FroalaEditor

from ..models.forum import Post


class StudentPostForm(forms.ModelForm):
    text = forms.CharField(widget=FroalaEditor)

    class Meta:
        model = Post
        fields = ('title', 'text')

    def __init__(self, *args, **kwargs):
        super(StudentPostForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "id_xxx"

    def clean_text(self):
        """
        If somebody enters into this form ' hello ',
        the extra whitespace will be stripped.
        """
        return self.cleaned_data.get('text', '').strip()

    def clean_title(self):
        """
        If somebody enters into this form ' hello ',
        the extra whitespace will be stripped.
        """
        return self.cleaned_data.get('title', '').strip()