import floppyforms.__future__ as forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from .models import Newsletter
from django_markdown.fields import MarkdownFormField
from django_markdown.widgets import MarkdownWidget
from pagedown.widgets import AdminPagedownWidget
from django import forms


class NewsletterCreateForm(forms.ModelForm):

    class Meta:
        model = Newsletter
        fields = ('title', 'excerpt', 'content', 'published')

    helper = FormHelper()
    helper.form_tag = True
    helper.form_show_labels = True


class NewsletterUpdateForm(forms.ModelForm):
    content = forms.CharField(widget=AdminPagedownWidget())

    class Meta:
        model = Newsletter
        fields = ('title', 'excerpt', 'content', 'published')

    helper = FormHelper()
    helper.form_tag = True
    helper.form_show_labels = True



