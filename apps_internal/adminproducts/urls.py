# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.conf.urls import patterns, url

from .views import CourseProductGroupUpdateView, PublicTextChunksUpdateView, \
    MentorsProfileUpdateView


urlpatterns = patterns('',
    url(r'^produktgruppe/(?P<pk>\d{1,4})/update$', CourseProductGroupUpdateView.as_view(),
        name='updategroup' ),

    url(r'^mentor/(?P<pk>\d{1,4})/update$',
        MentorsProfileUpdateView.as_view(),
        name='updatementor' ),

)

