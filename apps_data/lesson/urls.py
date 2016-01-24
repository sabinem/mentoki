# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, include, url

from .utils.lessoncopy import copy_block_for_courseevent
from .utils.lessontoblockcopy import copy_lesson_to_block


urlpatterns = patterns('',

    url(r'^copy/(?P<courseevent_pk>\d{1,4})/(?P<block_pk>\d{1,4})$',
        copy_block_for_courseevent, name="copy_block"),

    url(r'^copy/(?P<course_pk>\d{1,4})/(?P<lesson_pk>\d{1,4})/(?P<block_pk>\d{1,4})$',
        copy_lesson_to_block, name="copy_lesson_to_block"),

    )
