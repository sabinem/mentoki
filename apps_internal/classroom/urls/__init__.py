# -*- coding: utf-8 -*-

"""
Urls für das Klassenzimmer
- start ist der Startpunkt, der eingestellt werden kann
- forum ist selbsterklärend
- Unterricht: enthält auch Links zum Erstellen von Arbeiten, die sich auf
  einen Lernabschnitt beziehen
- aktuelles: sind die Ankündigungen
- student: Privatbereich des Schülers
- teilnehmerliste: Teilnehmerliste
"""

from __future__ import unicode_literals

from django.conf.urls import patterns, include, url

from ..views.start import ClassroomStartView


urlpatterns = patterns('',

    url(r'^$', ClassroomStartView.as_view(), name="start"),

    url(r'^forum/', include('apps_internal.classroom.urls.forum', namespace="forum")),

    url(r'^unterricht/', include('apps_internal.classroom.urls.classlesson', namespace='classlesson')),

    url(r'^aktuelles/', include('apps_internal.classroom.urls.announcement', namespace='announcement')),

    # Privatbereich des Schülers
    url(r'^student/', include('apps_internal.classroom.urls.studentswork', namespace='studentswork')),

    url(r'^aufgabe/', include('apps_internal.classroom.urls.homework', namespace='homework')),

    url(r'^teilnehmerliste/', include('apps_internal.classroom.urls.participant', namespace='participant')),
    )
