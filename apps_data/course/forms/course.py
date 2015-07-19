# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

import floppyforms.__future__ as forms

from apps_data.course.models import Course


class CourseTeachersChangeForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = ('title', 'excerpt', 'target_group', 'prerequisites', 'project',
                  'structure', 'text')

    def __init__(self, user=None, *args, **kwargs):
        super(CourseTeachersChangeForm, self).__init__(*args, **kwargs)
        if not self.instance.pk:
           raise forms.ValidationError(_("no permission to create a new course, ask administrator to do it for you."))
        else:
           course = self.instance
           if not course.owners.filter(pk=user.pk).exists():
              raise forms.ValidationError(_("no permission to work on that course."))

