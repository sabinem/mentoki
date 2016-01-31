# coding: utf-8

"""
Admin for MentorsProfile
"""

from __future__ import unicode_literals, absolute_import

from django.contrib import admin

from .models.mentor import MentorsProfile
from .models.notification import NotificationProfile


@admin.register(MentorsProfile)
class MentorsProfileAdmin(admin.ModelAdmin):
    """
    Courses are time independent collections of teaching material, that are
    set up and owned by teachers.
    """
    list_display = ('id', 'user', 'slug', 'modified', 'created')
    list_filter = ('modified',)
    list_display_links = ('id',)


@admin.register(NotificationProfile)
class NotficationProfileAdmin(admin.ModelAdmin):
    """
    Courses are time independent collections of teaching material, that are
    set up and owned by teachers.
    """
    list_display = ('id', 'user', 'courseevent', 'modified', 'classroom_all', 'announcements',
                    'forum_all', 'forum_involved',
                    'studentswork_all')
                    #'studentswork_involved')                                                                                         ')
    list_filter = ('modified', 'user', 'courseevent__course', 'courseevent')
    list_display_links = ('id',)
