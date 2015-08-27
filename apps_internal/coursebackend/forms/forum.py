# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import get_object_or_404
from django.core.validators import ValidationError

import floppyforms.__future__ as forms

from froala_editor.widgets import FroalaEditor

from apps_data.courseevent.models.forum import Forum
from apps_data.courseevent.models.courseevent import CourseEvent


class ForumForm(forms.ModelForm):
    text = forms.CharField(widget=FroalaEditor)

    class Meta:
        model = Forum
        fields = ('title', 'text', 'description', 'parent', 'display_nr', 'can_have_threads', 'hidden')

    def __init__(self, *args, **kwargs):
        courseevent_slug = kwargs.pop('courseevent_slug', None)
        self.courseevent = get_object_or_404(CourseEvent, slug=courseevent_slug)

        super(ForumForm, self).__init__(*args, **kwargs)

        self.fields["parent"].queryset = \
            Forum.objects.forums_for_courseevent(courseevent=self.courseevent)

    def clean_can_have_threads(self):
        if not self.cleaned_data['can_have_threads']:
            if self.instance.pk and self.instance.thread_count > 0:
                raise ValidationError('''Dieses Forum hat bereits Beiträge,
                deshalb müssen Beiträge erlaubt bleiben.''')
        return self.cleaned_data['can_have_threads']