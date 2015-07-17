import floppyforms.__future__ as forms
from django.forms import ModelForm
from .models import Newsletter
from pagedown.widgets import AdminPagedownWidget
from django import forms


class NewsletterEditForm(forms.ModelForm):
    content = forms.CharField(widget=AdminPagedownWidget())

    class Meta:
        model = Newsletter
        fields = ('title', 'excerpt', 'content', 'published')




