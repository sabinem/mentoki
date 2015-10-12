# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import floppyforms.__future__ as forms

from apps_data.courseevent.models.announcement import Announcement


class AnnouncementUpdateForm(forms.ModelForm):
    """
    used to create or update an announcement
    """
    class Meta:
        model = Announcement
        fields = ('title', 'text', 'published')
