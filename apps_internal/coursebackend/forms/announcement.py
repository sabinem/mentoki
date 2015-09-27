# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import floppyforms.__future__ as forms

from django.template.loader import get_template
from django.template import Context

from froala_editor.widgets import FroalaEditor

from mailqueue.models import MailerMessage

from apps_data.courseevent.models.announcement import Announcement
from apps_data.courseevent.models.courseevent import CourseEventParticipation
from apps_data.course.models.course import CourseOwner
from mentoki.settings import MENTOKI_INFO_EMAIL


class AnnouncementUpdateForm(forms.ModelForm):
    """
    used to create or update an announcement
    """
    class Meta:
        model = Announcement
        fields = ('title', 'text', 'published')
