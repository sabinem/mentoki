# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.core.validators import ValidationError

import floppyforms.__future__ as forms

from froala_editor.widgets import FroalaEditor

from apps_data.course.models.course import CourseOwner


class TeachersCourseProfileForm(forms.ModelForm):
    text = forms.CharField(widget=FroalaEditor)

    class Meta:
        model = CourseOwner
        fields = ('foto', 'text', 'display', 'display_nr' )

    def clean_display(self):
        print "----------- in clean_display"
        display = self.cleaned_data["display"]
        if not display:
            if not CourseOwner.objects.other_teachers_for_display(course=self.instance.course,
                                                                  user=self.instance.user):
                raise ValidationError('''Wenigstens ein Lehrerprofil pro Kurs muss in der Kurs-Ausschreibung
                                      angezeigt werden.''')
        return self.cleaned_data["display"]