# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from .views.courseproductgroup_info import \
    CourseGroupDetailView, CourseGroupMentorsView
from .views.courseproductgroup_list import CourseProductGroupsListView
from .views.courseproductgroup_sales import CourseGroupOfferView


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

