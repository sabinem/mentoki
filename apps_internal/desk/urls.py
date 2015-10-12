# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.conf.urls import patterns, url

from .views import DeskStartView, DeskTeachView, DeskLearnView, \
    DeskAdminView, DeskProfileView


urlpatterns = patterns('',
    url(r'^start$', DeskStartView.as_view(), name='start' ),

    url(r'^unterrichten$', DeskTeachView.as_view(), name='teach' ),

    url(r'^lernen$', DeskLearnView.as_view(), name='learn' ),

    url(r'^profile$', DeskProfileView.as_view(), name='profile' ),

    url(r'^admin$', DeskAdminView.as_view(), name='admin' ),

)

