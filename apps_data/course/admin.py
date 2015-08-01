# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.contrib import admin

from .models.course import Course, CourseOwner
from .models.lesson import Lesson, LessonPublisher
from .models.material import Material

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'teachersrecord', 'email', 'modified', 'teachers', 'teachersrecord')


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'lesson_nr', 'lesson_type', 'title', 'nr', 'is_block', 'level')
    list_filter = ('course', 'level')


@admin.register(LessonPublisher)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'courseevent', 'lesson', 'published')
    list_filter = ('courseevent', 'lesson', 'published')


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'document_type', 'file')
    list_filter = ('course',)


@admin.register(CourseOwner)
class CourseOwnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'user', 'modified')


# old models: will be deleted as soon as the data has been transfered
from .models.oldcoursepart import CourseBlock, CourseUnit, CourseMaterialUnit


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


