# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url, include

urlpatterns = patterns('apps_core.upload.views',
    url(r'^ajax/photos/upload/$', "upload_photos", name="upload_photos"),
    url(r'^ajax/photos/recent/$', "recent_photos", name="recent_photos"),
    url(r'^list/$', 'list', name='list')
)


