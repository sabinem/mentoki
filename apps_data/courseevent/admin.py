# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib import admin

from .models import CourseEvent, CourseeventUnitPublish, CourseEventParticipation, \
    Announcement, Forum, \
    Thread, Post
#old delete later on
from .models import CourseEventPubicInformation



@admin.register(CourseEvent)
class CourseEventAdmin(admin.ModelAdmin):
    list_display = ('slug', 'id', 'title', 'course', )
    list_filter =  ('course',)


@admin.register(CourseeventUnitPublish)
class CourseeventUnitPublishAdmin(admin.ModelAdmin):
    list_display = ('unit', 'courseevent')
    list_filter = ('unit', 'courseevent')


@admin.register(CourseEventParticipation)
class CourseEventParticipationAdmin(admin.ModelAdmin):
    list_display = ('user', 'courseevent')
    list_filter = ('user', 'courseevent')


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


# old
@admin.register(CourseEventPubicInformation)
class CourseEventPubicInformationAdmin(admin.ModelAdmin):
    list_display = ('id', 'courseevent',)
    list_filter = ('courseevent',)
