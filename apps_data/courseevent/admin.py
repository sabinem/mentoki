# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib import admin

from .models.announcement import Announcement
from .models.courseevent import CourseEvent, CourseEventParticipation
from .models.forum import Forum, Thread, Post
from .models.menu import ClassroomMenuItem
from .models.homework import StudentsWork


@admin.register(CourseEvent)
class CourseEventAdmin(admin.ModelAdmin):
    """
    courseevents
    """
    list_display = ('id', 'slug', 'title', 'course','students', 'teachers', 'workers', 'modified', 'created',
                    'event_type', 'status_external', 'status_internal')
    list_filter =  ('course',)


@admin.register(CourseEventParticipation)
class CourseEventParticipationAdmin(admin.ModelAdmin):
    """
    users as participants in a courseevent
    """
    list_display = ('id', 'user', 'courseevent', 'hidden')
    list_filter = ('user', 'courseevent')


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'courseevent', 'is_archived', 'published_at', 'published',
                    'mail_distributor', 'modified', 'created')
    list_filter = ('courseevent', 'published')


@admin.register(ClassroomMenuItem)
class ClassroomMenuItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'display_nr', 'display_title','is_forumlink',
                    'item_type', 'is_shortlink', 'is_publishlink', 'forum', 'classlesson',
                    'is_start_item', )
    list_filter = ('courseevent', )


@admin.register(StudentsWork)
class StudentsWorkAdmin(admin.ModelAdmin):
    list_display = ('id', 'courseevent', 'published_at', 'published', 'title', 'homework')
    list_filter = ('courseevent', 'homework', 'published')


@admin.register(Forum)
class ForumAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'courseevent', 'published', 'parent', 'decendants_thread_count', 'has_published_decendants' )
    list_filter = ( 'courseevent', 'published')


@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    list_display = ( 'id', 'courseevent', 'forum', 'title', 'post_count',
                     'author', 'last_author', 'modified', 'created')
    list_filter = ( 'courseevent', 'author', 'last_author')
    readonly_fields = ('modified', 'last_author' )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ( 'id', 'courseevent', 'thread', 'id', 'title', 'author', 'modified', 'created')
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

