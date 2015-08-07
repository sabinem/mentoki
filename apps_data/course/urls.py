# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, include, url

from django_downloadview import ObjectDownloadView

from apps_data.course.models.material import Material


# for the download of files
download = ObjectDownloadView.as_view(model=Material, file_field='file')

urlpatterns = patterns('',
    url(r'^download/(?P<slug>[a-zA-Z0-9_-]+)/$', download, name="download"),
    )