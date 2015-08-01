# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import floppyforms.__future__ as forms

from ..models.forum import Thread

from django.core.validators import ValidationError


class StudentThreadForm(forms.ModelForm):

    class Meta:
        model = Thread
        fields = ('title', 'text')

    def __init__(self, *args, **kwargs):
        super(StudentThreadForm, self).__init__(*args, **kwargs)

    def clean(self):
        """
        If somebody enters into this form ' hello ',
        the extra whitespace will be stripped.
        """
        raise ValidationError('all not good')
        return self.cleaned_data


    def clean_text(self):
        """
        If somebody enters into this form ' hello ',
        the extra whitespace will be stripped.
        """
        print "i am in threre clean Thread text +++++++"
        text = self.cleaned_data.get('text', '')


        raise ValidationError('text not good')
        return self.cleaned_data.get('text', '').strip()


    def clean_title(self):
        """
        If somebody enters into this form ' hello ',
        the extra whitespace will be stripped.
        """
        raise ValidationError('title not good')
        print "i am in here +++++++"
        return self.cleaned_data.get('title', '').strip()