# coding: utf-8

"""
Admin for Course and its relation to User: CourseOwner
"""

from __future__ import unicode_literals, absolute_import

from django.contrib import admin

from .models.courseevent import CourseEventProduct
from .models.simple import SimpleProduct


@admin.register(CourseEventProduct)
class CourseEventProductAdmin(admin.ModelAdmin):
    """
    Courses are time independent collections of teaching material, that are
    set up and owned by teachers.
    """
    list_display = ('id', 'courseevent', 'modified', 'created')
    list_filter = ('modified', 'courseevent')
    list_display_links = ('id',)


@admin.register(SimpleProduct)
class SimpleProductAdmin(admin.ModelAdmin):
    """
    Courses are time independent collections of teaching material, that are
    set up and owned by teachers.
    """
    list_display = ('id', 'name', 'modified', 'created')
    list_filter = ('modified', )
    list_display_links = ('id',)