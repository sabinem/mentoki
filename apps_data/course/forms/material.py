# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import floppyforms.__future__ as forms

from apps_data.course.models import Material


class MaterialForm(forms.ModelForm):

    class Meta:
        model = Material
        fields = ('excerpt',)

    def __init__(self, user=None, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
        if not self.instance.pk:
           raise forms.ValidationError(_("Course does not exist yet"))
        self.course = course

    def clean(self):
        cleaned_data = super(CourseForm, self).clean()
        return cleaned_data

    def save(self, commit=True):
        if not self.instance.pk:
            self.instance.course = self.course
        return super(CourseForm, self).save(commit)