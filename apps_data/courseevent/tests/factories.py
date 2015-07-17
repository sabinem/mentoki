# coding: utf-8

from __future__ import unicode_literals, absolute_import

from apps_data.course.models import Course, CourseOwner
from ..models import CourseEvent, CourseEventParticipation, Forum, Thread, Post, Announcement

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