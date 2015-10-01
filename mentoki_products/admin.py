# coding: utf-8

"""
Admin for Course and its relation to User: CourseOwner
"""

from __future__ import unicode_literals, absolute_import

from django.contrib import admin

from .models.courseeventproduct import CourseEventProduct


@admin.register(CourseEventProduct)
class CourseAdmin(admin.ModelAdmin):
    """
    Courses are time independent collections of teaching material, that are
    set up and owned by teachers.
    """
    list_display = ('id', 'courseevent', 'modified', 'created')
    list_filter = ('modified', 'courseevent')
    list_display_links = ('id',)
