# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from .views import CourseOfferDetailView, CourseOfferListView


urlpatterns = patterns('',

    url(r'^$', CourseOfferListView.as_view(), name='list'),

    url(r'^(?P<slug>[a-z0-9_-]{3,50})/$', CourseOfferDetailView.as_view(), name='detail'),

)

