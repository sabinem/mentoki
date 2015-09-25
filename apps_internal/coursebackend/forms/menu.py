# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.core.validators import ValidationError
from django.shortcuts import get_object_or_404

import floppyforms.__future__ as forms

from apps_data.courseevent.models.menu import ClassroomMenuItem
from apps_data.courseevent.models.courseevent import CourseEvent
from apps_data.courseevent.models.forum import Forum
from apps_data.lesson.models.classlesson import ClassLesson


class MenuItemForm(forms.ModelForm):

    class Meta:
        model = ClassroomMenuItem
        fields = ('display_nr', 'display_title', 'icon', 'item_type',
                  'classlesson', 'forum',
                  'is_start_item', 'is_shortlink')

    def __init__(self, *args, **kwargs):
        courseevent_slug = kwargs.pop('courseevent_slug', None)
        self.courseevent = get_object_or_404(CourseEvent, slug=courseevent_slug)

        super(MenuItemForm, self).__init__(*args, **kwargs)
        self.fields['classlesson'].queryset = \
            ClassLesson.objects.lessons_for_menu(courseevent=self.courseevent)
        self.fields['forum'].queryset = \
            Forum.objects.classroom_menu(courseevent=self.courseevent)


    def clean_display_title(self):
        if self.cleaned_data['display_title'] == "":
            raise ValidationError('''Der Eintrag muss beschriftet werden. ''')
        return self.cleaned_data["display_title"]

