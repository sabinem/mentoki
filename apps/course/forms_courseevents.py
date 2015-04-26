# coding: utf-8
import floppyforms.__future__ as forms
# import from django
from django.forms import ModelForm
# from 3rd party apps
from crispy_forms.helper import FormHelper
# import from this app
from apps.courseevent.models import CourseEventPubicInformation, CourseEvent

class CourseEventUpdateFormMixin(object):

    def __init__(self, *args, **kwargs):
        super(CourseEventUpdateFormMixin, self).__init__(*args, **kwargs)
        self.helper = FormHelper(form=self)
        self.helper.form_tag = False
        self.helper.form_show_labels = False


class CourseEventUpdateExcerptForm(CourseEventUpdateFormMixin, forms.ModelForm):

    class Meta:
        model = CourseEvent
        fields = ('excerpt',)


class CourseEventUpdateTextForm(CourseEventUpdateFormMixin, forms.ModelForm):
    class Meta:
        model = CourseEventPubicInformation
        fields = ('text',)


class CourseEventUpdateFormatForm(CourseEventUpdateFormMixin, forms.ModelForm):
    class Meta:
        model = CourseEventPubicInformation
        fields = ('format',)


class CourseEventUpdateWorkloadForm(CourseEventUpdateFormMixin, forms.ModelForm):
    class Meta:
        model = CourseEventPubicInformation
        fields = ('workload',)


class CourseEventUpdateProjectForm(CourseEventUpdateFormMixin, forms.ModelForm):
    class Meta:
        model = CourseEventPubicInformation
        fields = ('project',)


class CourseEventUpdatePrerequisitesForm(CourseEventUpdateFormMixin, forms.ModelForm):
    class Meta:
        model = CourseEventPubicInformation
        fields = ('prerequisites',)


class CourseEventUpdateStructureForm(CourseEventUpdateFormMixin, forms.ModelForm):
    class Meta:
        model = CourseEventPubicInformation
        fields = ('structure',)


class CourseEventUpdateTargetgroupForm(CourseEventUpdateFormMixin, forms.ModelForm):
    class Meta:
        model = CourseEventPubicInformation
        fields = ('target_group',)


class CourseEventUpdateVideoForm(CourseEventUpdateFormMixin, forms.ModelForm):
    class Meta:
        model = CourseEventPubicInformation
        fields = ('video_url',)
