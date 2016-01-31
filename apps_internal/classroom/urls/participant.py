# -*- coding: utf-8 -*-

"""
Urls für die Teilnehmerliste
- list: Liste aller sichtbaren (=aktiven) Teilnehmer
- detail: Detailansicht einer Ankündigung
"""

from __future__ import unicode_literals

from django.conf.urls import patterns, url

from ..views.participant import CourseParticipantListView

urlpatterns = patterns('',

    url(r'^$', CourseParticipantListView.as_view(),
        {'template':'classroom/participant/pages/list.html'}, name='list')
    )
