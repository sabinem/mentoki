# coding: utf-8

"""
Admin for MentorsProfile
"""

from __future__ import unicode_literals, absolute_import

from django.contrib import admin

from .models.mentor import MentorsProfile


@admin.register(MentorsProfile)
class MentorsProfileAdmin(admin.ModelAdmin):
    """
    Courses are time independent collections of teaching material, that are
    set up and owned by teachers.
    """
    list_display = ('id', 'user', 'modified', 'created')
    list_filter = ('modified',)
    list_display_links = ('id',)