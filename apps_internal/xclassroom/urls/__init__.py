# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, include, url


urlpatterns = patterns('',

    url(r'^forum/', include('apps_internal.classroom.urls.forum', namespace="forum")),

    url(r'^unterricht/', include('apps_internal.classroom.urls.lesson', namespace='lesson')),

    url(r'^aktuelles/', include('apps_internal.classroom.urls.annoncement', namespace='announcement'))

    )
