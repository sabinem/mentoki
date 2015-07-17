# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, url

from ..views import CourseEventDetailView, CourseEventUpdateView, \
    CourseEventPublicInformationUpdateView, CourseEventExcerptUpdateView


urlpatterns = patterns('',
    url(r'^$', CourseEventDetailView.as_view(), name='detail'),

    url(r'^parameter$',
        CourseEventUpdateView.as_view(), name='update'),

    url(r'^feld/abstrakt$',
        CourseEventExcerptUpdateView.as_view(), name='updateexcerpt'),

    url(r'^(?P<pk>\d+)/feld/(?P<field>[a-z_]+)$',
        CourseEventPublicInformationUpdateView.as_view(), name='update'),

    #url(r'^freischaltung/$', include('apps.course.urls.publish', namespace='publish')),

    #url(r'^forum/$', include('apps.course.urls.forum', namespace='forum')),

    #url(r'^nachrichten/$', include('apps.course.urls.announcement', namespace='announcement')),

)
