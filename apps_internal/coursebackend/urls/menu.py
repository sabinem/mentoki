# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, url

from ..views.menu import MenuListView, MenuItemCreateView, MenuItemDeleteView,\
   MenuUpdateView, MenuItemUpdateView


urlpatterns = patterns('',

    url(r'^$', MenuListView.as_view(),
        {'template':'coursebackend/menu/pages/list.html'}, name='list'),

    url(r'^(?P<pk>\d{1,4})/bearbeiten$', MenuUpdateView.as_view(),
        {'template':'coursebackend/menu/pages/bulkupdate.html'}, name='bulk_update'),

    url(r'^(?P<pk>\d{1,4})/bearbeiten$', MenuItemUpdateView.as_view(),
        {'template':'coursebackend/menu/pages/update.html'}, name='item_update'),

    url(r'^anlegen$', MenuItemCreateView.as_view(),
        {'template':'coursebackend/menu/pages/create.html'}, name='item_create'),

    url(r'^(?P<pk>\d{1,4})/loeschen$', MenuItemDeleteView.as_view(),
        {'template':'coursebackend/menu/pages/delete.html'}, name='item_delete'),

    )