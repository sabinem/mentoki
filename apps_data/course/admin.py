# coding: utf-8

"""
Admin for Course and its relation to User: CourseOwner
"""

from __future__ import unicode_literals, absolute_import

from django.contrib import admin

from .models.course import Course, CourseOwner


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    """
    Courses are time independent collections of teaching material, that are
    set up and owned by teachers.
    """
    list_display = ('id', 'title', 'modified', 'created', 'teachers')
    list_filter = ('modified',)
    list_display_links = ('id',)


@admin.register(CourseOwner)
class CourseOwnerAdmin(admin.ModelAdmin):
    """
    Owners (teachers) of the course along with their profiles as
    course-teachers
    """
    list_display = ('id', 'course', 'user', 'modified', 'created')
    list_filter = ('modified', 'course', 'user')
    list_display_links = ('id',)
