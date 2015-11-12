# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.conf.urls import patterns, url

from .views.redirect import DeskRedirectView
from .views.learn import DeskLearnView
from .views.teach import DeskTeachView
from .views.admin import DeskAdminView
from .views.profile import DeskProfileView


urlpatterns = patterns('',
    url(r'^profile$', DeskProfileView.as_view(), name='start' ),

    url(r'^profile$', DeskProfileView.as_view(), name='profile' ),

    url(r'^unterrichten$', DeskTeachView.as_view(), name='teach' ),

    url(r'^lernen$', DeskLearnView.as_view(), name='learn' ),

    url(r'^admin$', DeskAdminView.as_view(), name='admin' ),

    url(r'^redirect$', DeskRedirectView.as_view(), name='redirect' ),

)

