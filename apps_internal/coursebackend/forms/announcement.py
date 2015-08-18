# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import floppyforms.__future__ as forms

from froala_editor.widgets import FroalaEditor

from apps_data.courseevent.models.announcement import Announcement


class AnnouncementForm(forms.ModelForm):
    text = forms.CharField(widget=FroalaEditor)

    class Meta:
        model = Announcement
        fields = ('title', 'text', 'published')
