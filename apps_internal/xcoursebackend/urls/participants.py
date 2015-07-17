# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, url

from ..views import CourseParticipantsListView


urlpatterns = patterns('',
url(r'^(?P<slug>[a-z0-9_-]{3,50})/(?P<ce_slug>[a-z0-9_-]{3,50})/teilnehmer$',
        CourseParticipantsListView.as_view(), name='participantslist'),
)

