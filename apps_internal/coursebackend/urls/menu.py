# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, url

from ..views.menu import MenuItemCreateView, MenuItemDeleteView,\
   MenuItemUpdateView, MenuPreView, MenuUpdateView


urlpatterns = patterns('',

    url(r'^vorschau$', MenuPreView.as_view(),
        {'template':'coursebackend/menu/pages/preview.html'}, name='preview'),

    url(r'^(?P<pk>\d{1,4})/bearbeiten$', MenuItemUpdateView.as_view(),
        {'template':'coursebackend/menu/pages/update.html'}, name='update'),

    url(r'^anlegen$', MenuItemCreateView.as_view(),
        {'template':'coursebackend/menu/pages/create.html'}, name='create'),

    url(r'^punkt/(?P<pk>\d{1,4})/loeschen$', MenuItemDeleteView.as_view(),
        {'template':'coursebackend/menu/pages/delete.html'}, name='delete'),

    url(r'^umsortieren$', MenuUpdateView.as_view(),
        {'template':'coursebackend/menu/pages/sort.html'}, name='sort'),
    )