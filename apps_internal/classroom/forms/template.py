# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import floppyforms.__future__ as forms

from froala_editor.widgets import FroalaEditor
from django.core.validators import ValidationError

from apps_data.courseevent.models.forum import Post


class StudentPostForm(forms.ModelForm):
    text = forms.CharField(widget=FroalaEditor)

    class Meta:
        model = Post
        fields = ('title', 'text')

    def clean_text(self):
        """
        If somebody enters into this form ' hello ',
        the extra whitespace will be stripped.
        """
        return self.cleaned_data.get('text', '')

    def clean_title(self):
        """
        If somebody enters into this form ' hello ',
        the extra whitespace will be stripped.
        """
        return self.cleaned_data.get('title', '')

    def clean(self):
        """
        If somebody enters into this form ' hello ',
        the extra whitespace will be stripped.
        """
        return self.cleaned_data