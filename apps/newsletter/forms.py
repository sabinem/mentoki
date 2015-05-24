import floppyforms.__future__ as forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from .models import Newsletter
from django_markdown.fields import MarkdownFormField
from django_markdown.widgets import MarkdownWidget


class NewsletterCreateForm(forms.Form):
    content = forms.CharField(widget=MarkdownWidget())
    excerpt = MarkdownFormField()

    class Meta:
        model = Newsletter
        fields = ('title', 'excerpt', 'content', 'published')

    helper = FormHelper()
    helper.form_tag = True
    helper.form_show_labels = True


class NewsletterUpdateForm(forms.Form):
    content = forms.CharField(widget=MarkdownWidget())
    excerpt = MarkdownFormField()



    helper = FormHelper()
    helper.form_tag = True
    helper.form_show_labels = True



