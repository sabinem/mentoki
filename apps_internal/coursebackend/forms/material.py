# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import floppyforms.__future__ as forms

from froala_editor.widgets import FroalaEditor

from apps_data.course.models.material import Material
from django.shortcuts import get_object_or_404

from crispy_forms.helper import FormHelper
from apps_data.course.models.course import Course

class MaterialForm(forms.ModelForm):

    class Meta:
        model = Material
        fields = ('title', 'description', 'document_type', 'pdf_download_link', 'pdf_viewer', 'pdf_link', 'file')
