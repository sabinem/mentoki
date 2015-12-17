# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from django.views.decorators.cache import cache_page

from .views.info import \
    CourseGroupDetailView
from .views.list import CourseProductGroupsListView, \
    ListNowView, ListPreviewView, ListSingleView


urlpatterns = patterns('',
    url(r'^$',
        cache_page(60*60)(
            CourseProductGroupsListView.as_view()
        ),
        name='list'),

    url(r'^jetzt-buchbar$',
        cache_page(60*60)(
            ListNowView.as_view()
        ),
        name='list_now'),

    url(r'^vorschau$',
        cache_page(60*60)(
            ListPreviewView.as_view()
        ),
        name='list_preview'),

    url(r'^(?P<slug>[a-z0-9_-]{3,50})/$',
        cache_page(60*60)(
            CourseGroupDetailView.as_view()
        ),
        name='detail'),

    url(r'^(?P<pk>\d{1,4})/admin$',
        ListSingleView.as_view(),
        name='admin'),
)

