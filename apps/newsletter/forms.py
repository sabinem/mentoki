import floppyforms.__future__ as forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from .models import Newsletter

class NewsletterCreateForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ('title', 'excerpt', 'content', 'published')

    helper = FormHelper()
    helper.form_tag = True
    helper.form_show_labels = True


class NewsletterUpdateForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ('title', 'excerpt', 'content', 'published')

    helper = FormHelper()
    helper.form_tag = True
    helper.form_show_labels = True



