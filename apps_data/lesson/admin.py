# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.contrib import admin

from .models.lesson import Lesson
from .models.classlesson import ClassLesson


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    """
    Lessons are stored for the course as templates for the actual courseevents
    """
    list_display = ('id', 'course', 'lesson_nr', 'title', 'modified', 'created', 'lesson_type', 'level',
                    'cb_id', 'u_id', 'um_id' )
    list_filter = ('course', 'level', 'modified')



@admin.register(ClassLesson)
class ClassLessonAdmin(admin.ModelAdmin):
    """
    ClassLessons are copied into the courseevent from a lesson
    They can be further adapted in the courseevent.
    """
    list_display = ('id', 'courseevent', 'lesson_nr', 'title', 'published', 'org_lesson_id', 'modified', 'created', 'lesson_type', 'level')
    list_filter = ('courseevent', 'level', 'modified')