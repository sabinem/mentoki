import floppyforms.__future__ as forms
# import from django
from django.forms import ModelForm
# from 3rd party apps
from crispy_forms.helper import FormHelper
# import from this app
from .models import Course, CourseOwner


class CourseUpdateFormMixin(object):

    def __init__(self, *args, **kwargs):
        super(CourseUpdateFormMixin, self).__init__(*args, **kwargs)
        self.helper = FormHelper(form=self)
        self.helper.form_tag = False
        self.helper.form_show_labels = False


class CourseUpdateExcerptForm(CourseUpdateFormMixin, forms.ModelForm):

    class Meta:
        model = Course
        fields = ('excerpt',)


class CourseUpdateTextForm(CourseUpdateFormMixin, forms.ModelForm):
    class Meta:
        model = Course
        fields = ('text',)


class CourseUpdateTargetgroupForm(CourseUpdateFormMixin, forms.ModelForm):
    class Meta:
        model = Course
        fields = ('target_group',)


class CourseUpdatePrerequisitesForm(CourseUpdateFormMixin, forms.ModelForm):
    class Meta:
        model = Course
        fields = ('prerequisites',)


class CourseUpdateProjectForm(CourseUpdateFormMixin, forms.ModelForm):
    class Meta:
        model = Course
        fields = ('project',)


class CourseUpdateStructureForm(CourseUpdateFormMixin, forms.ModelForm):
    class Meta:
        model = Course
        fields = ('structure',)




