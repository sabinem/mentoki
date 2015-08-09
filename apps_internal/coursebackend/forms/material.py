# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.core.validators import ValidationError

import floppyforms.__future__ as forms

from apps_data.course.models.material import Material


class MaterialForm(forms.ModelForm):

    class Meta:
        model = Material
        fields = ('title', 'description', 'document_type', 'pdf_download_link', 'pdf_viewer', 'pdf_link', 'file')

    def clean_document_type(self):
        document_type = self.cleaned_data["document_type"]
        if document_type == Material.DOCTYPE.zip :
            raise ValidationError('''zip-Datein werden derzeit noch nicht unterstützt.''')
        return self.cleaned_data["document_type"]
