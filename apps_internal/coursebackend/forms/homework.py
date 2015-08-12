# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import get_object_or_404

import floppyforms.__future__ as forms

from froala_editor.widgets import FroalaEditor

from apps_data.course.models.lesson import Lesson
from apps_data.courseevent.models.homework import Homework
from apps_data.course.models.course import Course


class HomeworkForm(forms.ModelForm):
    text = forms.CharField(widget=FroalaEditor)

    class Meta:
        model = Homework
        fields = ('title', 'text', 'lesson', 'due_date')

    def __init__(self, *args, **kwargs):
        course_slug = kwargs.pop('course_slug', None)
        self.course = get_object_or_404(Course, slug=course_slug)

        super(HomeworkForm, self).__init__(*args, **kwargs)

        self.fields["lesson"].queryset = \
            Lesson.objects.lessons_for_course(course=self.course)