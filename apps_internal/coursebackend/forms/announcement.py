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


class AnnouncementForm(forms.ModelForm):
    text = forms.CharField(widget=FroalaEditor)

    class Meta:
        model = Announcement
        fields = ('title', 'text', 'published')

    CONTACT_EMAIL=MENTOKI_INFO_EMAIL

    def __init__(self, *args, **kwargs):
        super(AnnouncementForm, self).__init__(*args, **kwargs)

    def send_announcement(self):

        print "============================"
        print self.instance
        print self.data
        return