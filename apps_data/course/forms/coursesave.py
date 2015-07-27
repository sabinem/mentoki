# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

import floppyforms.__future__ as forms

from apps_data.course.models.course import Course


class CourseTeachersChangeForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = ('excerpt', 'target_group', 'prerequisites', 'project',
                  'structure', 'text')

    def __init__(self, form_user=None, update_field=None, *args, **kwargs):

        print "**********%%%%**** IN Form"
        print user
        print update_field
        print self.instance
        print "***_________***_________***________"
        """
        if user:
            self.form_user = user
        else:
            self.form_user = kwargs.pop('form_user', None)
        if update_field:
            self.update_field = update_field
        else:
            self.form_update_field = kwargs.pop('form_update_field', None)
        """
        super(CourseTeachersChangeForm, self).__init__(self, *args, **kwargs)

        if not self.form_user:
            raise forms.ValidationError(_("no user provided for access."), code="no_user")
        else:

            if not self.instance.pk:
               raise forms.ValidationError(_("no permission to create a new course, ask administrator to do it for you."),
                                           code='create_not_allowed')
            else:
               course = self.instance
               if not course.owners.filter(pk=self.form_user.pk).exists():
                  raise forms.ValidationError(_("no permission to work on that course."),code='not_owner')

        if self.update_field:
           if not self.update_field in self.fields:
              raise forms.ValidationError(_("wrong field for update"), code='field_not_for_update')
           else:
               if self.update_field != 'excerpt':
                   self.fields['excerpt'] = self.instance.excerpt
               if self.update_field != 'excerpt':
                   self.fields['target_group'] = self.instance.target_group


