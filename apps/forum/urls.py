from __future__ import unicode_literals
from django.conf.urls import patterns, url
from django.contrib import admin
admin.autodiscover()
# import from this app
from .views_forum import ForumListView, SubForumListView, ForumRecentListView
from .views_thread import ThreadCreateView, ThreadDeleteView, ThreadUpdateView, \
    PostUpdateView, PostDeleteView, ThreadListPostCreateView

urlpatterns = patterns('',

    # create thread

    #display thread with postupdateform
    url(r'^(?P<slug>[a-z0-9_-]{3,50})/forum/(?P<subforum>\d{1,4})/thread/(?P<thread>\d{1,4})/post/(?P<post>\d{1,4})/updatepost$', PostUpdateView.as_view(),
        name='updatepost'),

    #display thread with postdeleteform
    url(r'^(?P<slug>[a-z0-9_-]{3,50})/forum/(?P<subforum>\d{1,4})/thread/(?P<thread>\d{1,4})/post/(?P<post>\d{1,4})/deletepost$', PostDeleteView.as_view(),
        name='deletepost'),

    # update thread
    url(r'^(?P<slug>[a-z0-9_-]{3,50})/forum/(?P<subforum>\d{1,4})/thread/(?P<thread>\d{1,4})/updatethread$', ThreadUpdateView.as_view(),
        name='updatethread'),

    # delete thread
    url(r'^(?P<slug>[a-z0-9_-]{3,50})/forum/(?P<subforum>\d{1,4})/thread/(?P<thread>\d{1,4})/deletethread$', ThreadDeleteView.as_view(),
        name='deletethread'),
)
