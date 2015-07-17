# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, include, url

from django_downloadview import ObjectDownloadView

from apps_data.course.models import Material


# for the download of files
download = ObjectDownloadView.as_view(model=Material, file_field='file')

urlpatterns = patterns('',

    url(r'^vorlage/', include('apps_internal.coursebackend.urls.course', namespace="course")),

    url(r'^kurs/(?P<slug>[a-z0-9_-]+)/', include('apps_internal.coursebackend.urls.courseevent', namespace="courseevent")),

    url(r'^leitung/', include('apps_internal.coursebackend.urls.courseowner', namespace='courseowner')),

    url(r'^material/', include('apps_internal.coursebackend.urls.material', namespace='material')),

    url(r'^unterricht/', include('apps_internal.coursebackend.urls.lesson', namespace='lesson')),

    url(r'^download/(?P<slug>[a-zA-Z0-9_-]+)/$', download, name="download"),

    )
