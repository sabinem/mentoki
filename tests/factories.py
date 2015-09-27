# coding: utf-8

from __future__ import unicode_literals, absolute_import

from apps_data.course.models.course import Course
from django.contrib.sites.models import Site

from apps_data.course.tests.factories import CourseFactory
from apps_data.lesson.tests.factories import ClassLessonFactory

from apps_data.courseevent.models.courseevent import CourseEvent, CourseEventParticipation
from apps_data.courseevent.models.forum import Forum, Thread, Post
from apps_data.courseevent.models.announcement import Announcement

import factory


class CourseFactory(factory.DjangoModelFactory):
    class Meta:
        model = Course


class SiteFactory(factory.DjangoModelFactory):
    class Meta:
        model = Site


class CourseEventFactory(factory.DjangoModelFactory):
    class Meta:
        model = CourseEvent

    course = factory.SubFactory(CourseFactory)


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


class ClassroomMenuItemFactory(factory.DjangoModelFactory):
    class Meta:
        model = ClassroomMenuItem


class ForumMenuItemFactory(ClassroomMenuItemFactory):
    class Meta:
        model = ClassroomMenuItem

    forum = factory.SubFactory(ForumFactory)


class ClassLessonMenuItemFactory(ClassroomMenuItemFactory):
    class Meta:
        model = ClassroomMenuItem

    forum = factory.SubFactory(ClassLessonFactory)