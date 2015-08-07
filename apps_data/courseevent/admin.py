# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib import admin
from django import forms

from .models.announcement import Announcement
from .models.courseevent import CourseEvent, CourseEventParticipation
from .models.forum import Forum, Thread, Post
from .models.menu import ClassroomMenuItem
from .models.homework import Homework, StudentsWork


@admin.register(CourseEvent)
class CourseEventAdmin(admin.ModelAdmin):
    list_display = ('slug', 'id', 'title', 'course', )
    list_filter =  ('course',)


@admin.register(CourseEventParticipation)
class CourseEventParticipationAdmin(admin.ModelAdmin):
    list_display = ('user', 'courseevent')
    list_filter = ('user', 'courseevent')


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('courseevent', 'published_at', 'published', 'created')
    list_filter = ('courseevent', 'published')


@admin.register(ClassroomMenuItem)
class ClassroomMenuItemAdmin(admin.ModelAdmin):
    list_display = ('courseevent', 'is_start_item', 'published', 'display_title', 'display_nr', 'item_type', 'forum', 'lesson', 'homework')
    list_filter = ('courseevent', )



@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    list_display = ('id', 'courseevent', 'title', 'due_date', 'published', 'lesson' )
    list_filter = ('courseevent', 'published')


@admin.register(StudentsWork)
class StudentsWorkAdmin(admin.ModelAdmin):
    list_display = ('id', 'courseevent', 'published_at', 'published', 'title', 'homework')
    list_filter = ('courseevent', 'homework', 'published')


@admin.register(Forum)
class ForumAdmin(admin.ModelAdmin):
    list_display = ('title', 'courseevent', 'id', 'published', 'parent' )
    list_filter = ( 'courseevent', 'published')
    list_display_links =  ('courseevent','title')


@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    list_display = ( 'courseevent', 'forum', 'id', 'title', 'post_count',
                     'author', 'last_author', 'modified', 'created')
    list_filter = ( 'courseevent', 'author', 'last_author')
    list_display_links  = ( 'title',)
    readonly_fields = ('modified', 'last_author' )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ( 'courseevent', 'thread', 'id', 'title', 'author', 'modified', 'created')
    list_filter = ( 'courseevent', 'author' )


#old delete later on
from .models.xmodelsold import CourseEventPubicInformation, CourseeventUnitPublish


@admin.register(CourseEventPubicInformation)
class CourseEventPubicInformationAdmin(admin.ModelAdmin):
    list_display = ('id', 'courseevent',)
    list_filter = ('courseevent',)


@admin.register(CourseeventUnitPublish)
class CourseeventUnitPublishAdmin(admin.ModelAdmin):
    list_display = ('unit', 'courseevent')
    list_filter = ('unit', 'courseevent')

