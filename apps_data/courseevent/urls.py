# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, include, url

from .utils.copycourse import copy_course_description


urlpatterns = patterns('',

    url(r'^copy/(?P<courseevent_pk>\d{1,4})$', copy_course_description, name="copydescription")
    )