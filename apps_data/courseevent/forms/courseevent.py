# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

import floppyforms.__future__ as forms

from django.utils.translation import ugettext_lazy as _

from apps_data.course.models.course import Course

ALLOWED_CHANGE_FIELDS_COURSE = ['title', 'excerpt', 'target_group', 'prerequisites', 'project',
                  'structure', 'text']

class CourseTeachersChangeForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = ('title', 'excerpt', 'target_group', 'prerequisites', 'project',
                  'structure', 'text')
