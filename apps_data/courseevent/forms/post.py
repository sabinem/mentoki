# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import floppyforms.__future__ as forms

from django.utils.translation import ugettext_lazy as _

from apps_data.course.models.material import Material


class MaterialForm(forms.ModelForm):

    class Meta:
        model = Material
        fields = ('title', 'description', 'document_type', 'pdf_download', 'pdf_viewer', 'pdf_link',
                  'file')

    def __init__(self, user=None, course=None, *args, **kwargs):
        super(MaterialForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
           course = self.instance.course
        if not course.owners.filter(pk=user.pk).exists():
           raise forms.ValidationError(_("no permission to work on that course."))

    def clean(self):
        cleaned_data = super(CourseForm, self).clean()
        return cleaned_data

    def save(self, commit=True):
        if not self.instance.pk:
            self.instance.course = self.course
        return super(CourseForm, self).save(commit)


class CourseTeachersChangeForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = ('title', 'excerpt', 'target_group', 'prerequisites', 'project',
                  'structure', 'text')

    def __init__(self, *args, **kwargs):
        self.update_field = kwargs.pop('update_field', None)
        self.user = kwargs.pop('user', None)
        self.fields = ('excerpt',)
        super(CourseTeachersChangeForm, self).__init__(*args, **kwargs)
        #if not self.instance.pk:
        #   raise forms.ValidationError(_("no permission to create a new course, ask administrator to do it for you."))
        #else:
        #   course = self.instance
        #   if not user:
        #       raise forms.ValidationError(_("no user provided."))
        #   else:
        #      if not course.owners.filter(pk=user.pk).exists():
        #          raise forms.ValidationError(_("no permission to work on that course."))
