# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.contrib import admin

from .models.lesson import Lesson


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'lesson_nr', 'lesson_type', 'title', 'nr', 'is_block', 'level')
    list_filter = ('course', 'level')


