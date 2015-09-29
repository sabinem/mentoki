# -*- coding: utf-8 -*-

"""
Form for entering a profile for the teachers that relates to the course
it contains a foto, a text about his qualification.

The other two attributes display(Bool) and display_nr are needed for
displaying the profile on the public page of the courseevents. The display_nr
controls which teacher is first in the combined namestring "taught by ..."
Display controls which teacher is shown on the public course page. One teachers
profile must be visible publically, but the second teachers profile may or may
not be shown.
"""

from __future__ import unicode_literals

from django.core.validators import ValidationError

import floppyforms.__future__ as forms

from froala_editor.widgets import FroalaEditor

from apps_data.course.models.course import CourseOwner


class TeachersCourseProfileForm(forms.ModelForm):
    """
    Form for entering the teachers prfoile and uploading his or her foto.
    """
    text = forms.CharField(widget=FroalaEditor)

    class Meta:
        model = CourseOwner
        fields = ('foto', 'text', 'display', 'display_nr' )

    def clean_display(self):
        """
        it is checked that at least one teacher will be publically visible
        """
        display = self.cleaned_data["display"]
        if not display:
            if not CourseOwner.objects.other_teachers_for_display(
                    course=self.instance.course,
                    user=self.instance.user):
                raise ValidationError('''Wenigstens ein Lehrerprofil pro
                Kurs muss in der Kurs-Ausschreibung
                angezeigt werden.''')
        return self.cleaned_data["display"]