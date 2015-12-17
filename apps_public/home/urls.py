# -*- coding: utf-8 -*-

"""
mentoki urls : should be maintained from the old site
"""

from django.conf.urls import patterns, url
from django.views.decorators.cache import cache_page

from .views import HomePageView,  \
    MentorsPageView, MentorsListView, \
    PublicPageView

urlpatterns = patterns("",

    url(r'^$',
        HomePageView.as_view(),
        name='home'),

    url(r'^mentor/(?P<slug>[a-z0-9_-]+)/$',
        MentorsPageView.as_view(),
        name='mentor'),

    url(r'^mentoren-team/$',
        MentorsListView.as_view(),
        name='mentorslist'),

    url(r'^(?P<slug>[a-z0-9_-]+)/$',
        #cache_page(60*60)(
            PublicPageView.as_view(),
        #),
        name='public'),

)