import floppyforms.__future__ as forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
# import from this app
from .models import CourseOwner


class CourseOwnerUpdateForm(forms.ModelForm):
    class Meta:
        model = CourseOwner
        fields = ('text', 'foto')

    def __init__(self, *args, **kwargs):
        super(CourseOwnerUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(form=self)
        self.helper.form_tag = False
        self.helper.form_show_labels = False




