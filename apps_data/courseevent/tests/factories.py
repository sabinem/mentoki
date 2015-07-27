# coding: utf-8

from __future__ import unicode_literals, absolute_import

from apps_data.course.models.course import Course, CourseOwner
from ..models.courseevent import CourseEvent, CourseEventParticipation
from ..models.forum import Forum, Thread, Post
from ..models.announcement import Announcement

import factory


class CourseEventFactory(factory.DjangoModelFactory):
    class Meta:
        model = CourseEvent


class AnnouncementFactory(factory.DjangoModelFactory):
    class Meta:
        model = Announcement


class ForumFactory(factory.DjangoModelFactory):
    class Meta:
        model = Forum


class ThreadFactory(factory.DjangoModelFactory):
    class Meta:
        model = Thread


class PostFactory(factory.DjangoModelFactory):
    class Meta:
        model = Post


class ParticipationFactory(factory.DjangoModelFactory):
    class Meta:
        model = CourseEventParticipation