# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.conf.urls import patterns, url

from .views.redirect import DeskRedirectView
from .views.learn import DeskLearnView
from .views.teach import DeskTeachView
from .views.pageadmin import PageAdminView
from .views.courseadmin import CourseAdminView
from .views.userprofile import UserProfileView
from .views.bookings import BookingsView

from .views.updates import CourseProductGroupUpdateView, PublicPagesUpdateView, \
    MentorsProfileUpdateView, UserProfileUpdateView


urlpatterns = patterns('',
    #url(r'^profil$', DeskProfileView.as_view(), name='start' ),

    url(r'^benutzerprofil$', UserProfileView.as_view(), name='userprofile' ),

    url(r'^unterrichten$', DeskTeachView.as_view(), name='teach' ),

    url(r'^lernen$', DeskLearnView.as_view(), name='learn' ),

    url(r'^webseite$', PageAdminView.as_view(), name='pageadmin' ),

    url(r'^kursauschreibungen$', CourseAdminView.as_view(), name='courseadmin' ),

    url(r'^kursbuchungen$', BookingsView.as_view(), name='bookings' ),

    url(r'^redirect$', DeskRedirectView.as_view(), name='redirect' ),

    url(r'^produktgruppe/(?P<pk>\d{1,4})/update$', CourseProductGroupUpdateView.as_view(),
        name='updategroup' ),

    url(r'^mentor/(?P<pk>\d{1,4})/update$',
        MentorsProfileUpdateView.as_view(),
        name='updatementor' ),

    url(r'^seite/(?P<pk>\w{1,20})/update$',
        PublicPagesUpdateView.as_view(),
        name='updatepage' ),

    url(r'^benutzerdaten/(?P<pk>\w{1,20})/update$',
        UserProfileUpdateView.as_view(),
        name='updateprofile' ),

)

