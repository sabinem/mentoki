# coding: utf-8

from __future__ import unicode_literals, absolute_import

# import from django
from django.contrib import admin
# import from own app
from .models import Course, CourseBlock, CourseUnit, CourseMaterialUnit, CourseOwner
from .models import Course, CourseOwner, Lesson, Material, ContentBlock

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'email', 'modified')


@admin.register(CourseOwner)
class CourseOwnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'user', 'modified')


@admin.register(ContentBlock)
class ContentBlockAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', )


@admin.register(Lesson)
class CourseOwnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'nr', 'title', 'lesson_nr',)
    list_filter = ('course',)


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')


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



