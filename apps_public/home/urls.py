# -*- coding: utf-8 -*-

"""
mentoki urls : should be maintained from the old site
"""

from django.conf.urls import patterns, url

from .views import HomePageView, AboutPageView, \
    MentorsPageView, StandardPageView, AGBPageView, MentorsListView, \
    ImpressumPageView, StarterkursPageView, TeachOnlinePageView,  \
    CourseReadyPageView, EducationMentoringPageView, PublicPageView

urlpatterns = patterns("",

    url(r'^$',
        HomePageView.as_view(),
        name='home'),

    url(r'^team$',
        AboutPageView.as_view(),
        name='about'),

    url(r'^mentor/(?P<slug>[a-z0-9_-]+)/$',
        MentorsPageView.as_view(),
        name='mentor'),

    url(r'^mentoren-team/$',
        MentorsListView.as_view(),
        name='mentorslist'),

    url(r'^(?P<slug>[a-z0-9_-]+)/$',
        PublicPageView.as_view(),
        name='public'),

)