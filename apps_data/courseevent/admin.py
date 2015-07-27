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
    list_filter = ('courseevent',)


@admin.register(ClassroomMenuItem)
class ClassroomMenuItemAdmin(admin.ModelAdmin):
    list_display = ('courseevent', 'is_start_item', 'published', 'display_nr', 'item_type', 'display_title')
    list_filter = ('courseevent', )



@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    list_display = ('courseevent', 'due_date', 'title')
    list_filter = ('courseevent',)


@admin.register(StudentsWork)
class StudentsWorkAdmin(admin.ModelAdmin):
    list_display = ('courseevent', 'published_at', 'published', 'title', 'homework')
    list_filter = ('courseevent', 'homework')


@admin.register(Forum)
class ForumAdmin(admin.ModelAdmin):
    list_display = ('title', 'courseevent', 'id', 'parent' )
    list_filter = ( 'courseevent', )
    list_display_links =  ('courseevent','title')


@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    list_display = ('modified', 'id', 'forum','title', 'forum')
    list_filter = ( 'forum' ,  'author')
    list_display_links  = ( 'forum',)
    readonly_fields = ('modified', )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('modified',  'id', 'thread', 'author', 'created')
    list_filter = ( 'thread__forum',  'author' )


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

