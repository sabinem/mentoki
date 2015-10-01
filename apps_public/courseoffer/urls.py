# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from .views import CourseEventProductView, CourseEventListView, ChristineView


urlpatterns = patterns('',

    url(r'^$',
        CourseEventListView.as_view(), name='list'),

    url(r'^selbstfuehrung$',
        ChristineView.as_view(), name='christine'),

    url(r'^(?P<slug>[a-z0-9_-]{3,50})/$',
        CourseEventProductView.as_view(), name='detail'),

)

