# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.contrib import admin

from .models.course import Course, CourseOwner

# old models: will be deleted as soon as the data has been transfered
from .models.oldcoursepart import CourseBlock, CourseUnit, CourseMaterialUnit


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    """
    courses are time independent collections of teaching material, that are
    set up and owned by teachers.
    """
    list_display = ('id', 'title', 'modified', 'created', 'teachers', 'email')
    list_filter = ('modified',)
    list_display_links = ('id',)


@admin.register(CourseOwner)
class CourseOwnerAdmin(admin.ModelAdmin):
    """
    owners (teachers) of the course along with their profiles that go with the course
    """
    list_display = ('id', 'course', 'user', 'modified', 'created')
    list_filter = ('modified', 'course', 'user')
    list_display_links = ('id',)

# old data: admis will be deleted

@admin.register(CourseBlock)
class CourseBlockAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'title', 'is_numbered')
    list_filter = ('course',)
    list_display_links = ('title',)


@admin.register(CourseUnit)
class CourseUnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'block', 'title')
    list_filter = ('course', 'block')
    list_display_links = ('title',)


@admin.register(CourseMaterialUnit)
class CourseMaterialUnitAdmin(admin.ModelAdmin):
    list_display = ('file', 'course', 'unit', 'title', )
    list_filter = ('course', 'unit')
    list_display_links = ('title',)


