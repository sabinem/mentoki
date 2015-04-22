import floppyforms.__future__ as forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from .models import CourseUnit, CourseBlock, CourseMaterialUnit
from apps.forum.models import SubForum


class SubForumForm(forms.ModelForm):

    class Meta:
        model = SubForum
        fields = ('title', 'text', 'parentforum', 'display_nr', 'can_have_threads')

    def __init__(self, *args, **kwargs):
        forum_id = kwargs.pop('forum_id', None)
        super(SubForumForm, self).__init__(*args, **kwargs)
        initial = kwargs.get('initial', {})
        self.helper = FormHelper(form=self)
        self.helper.form_tag = False
        self.helper.form_show_labels = True
        choice_qs = SubForum.objects.filter(forum_id=forum_id)
        self.fields['parentforum'].queryset = choice_qs