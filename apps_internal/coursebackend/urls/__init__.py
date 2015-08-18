# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, include, url


urlpatterns = patterns('',

    url(r'^vorlage/',
        include('apps_internal.coursebackend.urls.course', namespace="course")),

    url(r'^kursereignis/',
        include('apps_internal.coursebackend.urls.courseevent', namespace="courseevent")),

    url(r'^kursliste/',
        include('apps_internal.coursebackend.urls.courseeventslist', namespace="courseevents")),

    url(r'^leitung/',
        include('apps_internal.coursebackend.urls.courseowner', namespace='courseowner')),

    url(r'^material/',
        include('apps_internal.coursebackend.urls.material', namespace='material')),

    url(r'^unterricht/',
        include('apps_internal.coursebackend.urls.lesson', namespace='lesson')),

    url(r'^kurs/(?P<slug>[a-z0-9_-]+)/unterricht/',
        include('apps_internal.coursebackend.urls.classlesson', namespace='classlesson')),

    url(r'^kurs/(?P<slug>[a-z0-9_-]+)/teilnehmer/',
        include('apps_internal.coursebackend.urls.participant', namespace='participant')),

    url(r'^kurs/(?P<slug>[a-z0-9_-]+)/forum/',
        include('apps_internal.coursebackend.urls.forum', namespace='forum')),

    url(r'^kurs/(?P<slug>[a-z0-9_-]+)/ankuendigungen/',
        include('apps_internal.coursebackend.urls.announcement', namespace='announcement')),

    url(r'^kurs/(?P<slug>[a-z0-9_-]+)/aufgaben/',
        include('apps_internal.coursebackend.urls.homework', namespace='homework')),

    url(r'^kurs/(?P<slug>[a-z0-9_-]+)/menu/',
        include('apps_internal.coursebackend.urls.menu', namespace='menu')),
    )
