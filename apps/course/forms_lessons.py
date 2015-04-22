import floppyforms.__future__ as forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from .models import CourseUnit, CourseBlock, CourseMaterialUnit


class BlockForm(forms.ModelForm):

    class Meta:
        model = CourseBlock
        fields = ('title', 'status', 'is_numbered', 'show_full', 'display_nr', 'text')

    def __init__(self, *args, **kwargs):
        super(BlockForm, self).__init__(*args, **kwargs)
        initial = kwargs.get('initial', {})
        self.helper = FormHelper(form=self)
        self.helper.form_tag = False
        self.helper.form_show_labels = True


class UnitForm(forms.ModelForm):

    class Meta:
        model = CourseUnit
        fields = ('block', 'title', 'status', 'description', 'display_nr', 'text')

    def __init__(self, *args, **kwargs):
        super(UnitForm, self).__init__(*args, **kwargs)
        initial = kwargs.get('initial', {})
        self.helper = FormHelper(form=self)
        self.helper.form_tag = False
        self.helper.form_show_labels = True
        # only blocks from the same course can be associated
        self.fields['block'].queryset = CourseBlock.objects.filter(course_id=initial['course_id']).\
            order_by('display_nr')


class MaterialForm(forms.ModelForm):

    class Meta:
        fields = ('unit', 'title', 'status', 'description', 'display_nr', 'text', 'document_type', 'file')
        model = CourseMaterialUnit

    def __init__(self, *args, **kwargs):
        super(MaterialForm, self).__init__(*args, **kwargs)
        initial = kwargs.get('initial', {})
        self.helper = FormHelper(form=self)
        self.helper.form_tag = False
        self.helper.form_show_labels = True
        # only blocks from the same course can be associated
        self.fields['unit'].queryset = CourseUnit.objects.filter(course_id=initial['course_id']).\
            order_by('block','display_nr')