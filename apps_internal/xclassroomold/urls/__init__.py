# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, include, url

from ..views.start import ClassroomStartView


urlpatterns = patterns('',

    url(r'^klassenzimmer$', ClassroomStartView.as_view(), namespace="start"),

    #url(r'^forum/', include('apps_internal.classroom.urls.forum', namespace="forum")),

    #url(r'^unterricht/', include('apps_internal.classroom.urls.lesson', namespace='lesson')),

    #url(r'^aktuelles/', include('apps_internal.classroom.urls.annoncement', namespace='announcement'))

    )
