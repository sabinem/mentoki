# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import get_object_or_404

import floppyforms.__future__ as forms

from crispy_forms.helper import FormHelper

from apps.course.models import Material, Course


class MaterialForm(forms.ModelForm):

    class Meta:
        model = Material
        fields = ('title', 'description', 'document_type', 'pdf_download_link', 'pdf_viewer', 'pdf_link', 'file')

    def __init__(self, *args, **kwargs):

        course_slug = kwargs.pop('course_slug', None)
        course = get_object_or_404(Course, slug=course_slug)

        super(MaterialForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False

