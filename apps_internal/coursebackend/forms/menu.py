# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.core.validators import ValidationError
from django.shortcuts import get_object_or_404

import floppyforms.__future__ as forms

from apps_data.courseevent.models.menu import ClassroomMenuItem
from apps_data.courseevent.models.courseevent import CourseEvent
from apps_data.course.models.course import Course
from apps_data.courseevent.models.homework import Homework
from apps_data.courseevent.models.forum import Forum
from apps_data.course.models.lesson import Lesson


class MenuItemForm(forms.ModelForm):

    class Meta:
        model = ClassroomMenuItem
        fields = ('display_nr', 'display_title', 'item_type',
                  'lesson', 'forum', 'homework',
                  'is_start_item')

    def __init__(self, *args, **kwargs):
        courseevent_slug = kwargs.pop('courseevent_slug', None)
        self.courseevent = get_object_or_404(CourseEvent, slug=courseevent_slug)
        self.course = self.courseevent.course

        super(MenuItemForm, self).__init__(*args, **kwargs)

        self.fields['lesson'].queryset = Lesson.objects.lessons_for_course(course=self.course)
        self.fields['homework'].queryset = Homework.objects.filter(courseevent=self.courseevent)
        self.fields['forum'].queryset = Forum.objects.filter(courseevent=self.courseevent)