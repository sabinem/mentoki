# -*- coding: utf-8 -*-

"""
urls for the homepage and other public pages
"""

from django.conf.urls import patterns, url

from .views import HomePageView,  \
    MentorsPageView, MentorsListView, \
    PublicPageView

urlpatterns = patterns("",

    # mentoki homepage
    url(r'^$',
        HomePageView.as_view(),
        name='home'),

    # single mentor page
    url(r'^mentor/(?P<slug>[a-z0-9_-]+)/$',
        MentorsPageView.as_view(),
        name='mentor'),

    # list of all mentors
    url(r'^mentoren-team/$',
        MentorsListView.as_view(),
        name='mentorslist'),

    # all other public pages
    url(r'^(?P<slug>[a-z0-9_-]+)/$',
        PublicPageView.as_view(),
        name='public'),

)