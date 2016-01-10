# coding: utf-8

"""
Admin for MentorsProfile
"""

from __future__ import unicode_literals, absolute_import

from django.contrib import admin

from .models.classroomnotification import ClassroomNotification


@admin.register(ClassroomNotification)
class ClassroomNotificationAdmin(admin.ModelAdmin):
    """
    Courses are time independent collections of teaching material, that are
    set up and owned by teachers.
    """
    list_display = ('id', 'modified', 'created')
    list_filter = ('created',)
