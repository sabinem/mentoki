from __future__ import unicode_literals
import floppyforms.__future__ as forms

from django.forms import ModelForm
from django.db import models
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms.bootstrap import TabHolder, Tab, InlineField, PrependedText
from apps.forum.models import Thread


class ThreadCreateForm(forms.ModelForm):

    class Meta:
        model = Thread
        fields = ('title', 'text', )

    helper = FormHelper()
    helper.form_tag = False
    helper.form_show_labels = False




