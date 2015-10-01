# -*- coding: utf-8 -*-

"""
Admin for CourseEvents, Participation, and related components.
As such there are
* Announcements: send out as emails to the class
* Menuitems: that compose the classroom menu
* Studentsworks: that students do and turn in as assignements
* Forums: where students and teachers interact
* Threads: Part of the Forum
* Post: Part of a Forum: responses to threads.
"""

from __future__ import unicode_literals

from django.contrib import admin

from .models.announcement import Announcement
from .models.courseevent import CourseEvent, CourseEventParticipation
from .models.forum import Forum, Thread, Post
from .models.menu import ClassroomMenuItem
from .models.homework import StudentsWork
from apps_data.lesson.admin import LessonAdmin


@admin.register(CourseEvent)
class CourseEventAdmin(admin.ModelAdmin):
    """
    CourseEvents are the actual Events associated with Courses.
    """
    list_display = ('id', 'slug', 'title', 'course', 'teachersrecord',
                    'modified', 'created',
                    'event_type', 'status_external', 'status_internal')
    list_filter =  ('course','status_external', 'modified')


@admin.register(CourseEventParticipation)
class CourseEventParticipationAdmin(admin.ModelAdmin):
    """
    Here the relationship between users and Courseevents is established:
    the participation as students.
    """
    list_display = ('id', 'user', 'courseevent', 'hidden')
    list_filter = ('user', 'courseevent', 'modified')


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    """
    Announcements are the few-to-many communication from teachers to the class
    """
    list_display = ('id', 'title', 'courseevent', 'is_archived',
                    'published_at', 'published',
                    'mail_distributor', 'modified', 'created')
    list_filter = ('courseevent', 'published', 'modified')


@admin.register(ClassroomMenuItem)
class ClassroomMenuItemAdmin(admin.ModelAdmin):
    """
    Teachers establish there own menu for the classroom.
    """
    list_display = ('id', 'display_nr', 'display_title',
                    'item_type', 'is_shortlink', 'forum', 'classlesson',
                    'is_start_item', )
    list_filter = ('courseevent','modified' )


@admin.register(StudentsWork)
class StudentsWorkAdmin(admin.ModelAdmin):
    """
    Teachers can assign work to students. Then students can draft the
    assignements alone or in teams in privacy and turn them in to the class
    once they are ready.
    """
    list_display = ('id', 'courseevent', 'publish_count', 'republished_at',
                    'published_at', 'published', 'title', 'homework')
    list_filter = ('courseevent', 'homework', 'published', 'modified')


@admin.register(Forum)
class ForumAdmin(admin.ModelAdmin):
    """
    A Forum serves for the communication in class.
    """
    list_display = ( 'title', 'display_nr', 'tree_id','lft', 'rght', 'level' )
    list_filter = ( 'courseevent','level', 'modified')

@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    """
    The forum has threads.
    """
    list_display = ( 'id', 'courseevent', 'forum', 'title', 'post_count',
                     'author', 'last_author', 'modified', 'created')
    list_filter = ( 'courseevent', 'author', 'modified')
    readonly_fields = ('modified', 'last_author' )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    The threads in the forum have posts.
    """
    list_display = ( 'id', 'courseevent', 'thread', 'id', 'title', 'author', 'modified', 'created')
    list_filter = ( 'courseevent', 'author', 'modified')

