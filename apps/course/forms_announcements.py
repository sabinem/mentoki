import floppyforms.__future__ as forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from apps.classroom.models import Announcement

class AnnouncementCreateForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ('title', 'text', 'published')

    helper = FormHelper()
    helper.form_tag = True
    helper.form_show_labels = True


class AnnouncementUpdateForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ('title', 'text', 'published')

    helper = FormHelper()
    helper.form_tag = True
    helper.form_show_labels = True



