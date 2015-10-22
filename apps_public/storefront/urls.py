# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from .views.info import CourseProductGroupsListView, \
    CourseGroupDetailView, CourseGroupMentorsView, CourseGroupOfferView



urlpatterns = patterns('',

    url(r'^$',
        CourseProductGroupsListView.as_view(), name='list'),

    url(r'^(?P<slug>[a-z0-9_-]{3,50})/$',
        CourseGroupDetailView.as_view(), name='detail'),

    url(r'^(?P<slug>[a-z0-9_-]{3,50})/angebot$',
        CourseGroupOfferView.as_view(), name='offer'),

    url(r'^(?P<slug>[a-z0-9_-]{3,50})/kursleitung$',
        CourseGroupMentorsView.as_view(), name='mentors'),

)
