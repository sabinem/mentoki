from __future__ import unicode_literals
import floppyforms.__future__ as forms
from django.forms import ModelForm
from django.db import models
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms.bootstrap import InlineField
from .models import Post


class PostLayout(Layout):

   def __init__(self, *args, **kwargs):
        super(PostLayout, self).__init__(
            InlineField(
                'text',
            ),
        )


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text',)
    class Media:
        pass

    helper = FormHelper()
    helper.form_tag = False
    helper.form_show_labels = False
    helper.layout = Layout(
        PostLayout(),
    )


class PostUpdateForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('text',)

    class Media:
        pass

    helper = FormHelper()
    helper.form_tag = False
    helper.form_show_labels = False
    helper.layout = Layout(
        PostLayout(),
    )




