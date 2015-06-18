# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, url




# for the download of files
#download = ObjectDownloadView.as_view(model=CourseMaterialUnit, file_field='file')


urlpatterns = patterns('',
    #url(r'^block/$', include('apps.course.urls.block', namespace='block')),
    #url(r'^lektion/$', include('apps.course.urls.lesson', namespace='lesson')),
    #url(r'^material/$', include('apps.course.urls.material', namespace='material')),
)
