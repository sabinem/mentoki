# coding: utf-8

from __future__ import unicode_literals, absolute_import

from apps_data.course.tests.factories import CourseFactory
from apps_data.lesson.tests.factories import ClassLessonFactory

from ..models.courseevent import CourseEvent, CourseEventParticipation
from ..models.forum import Forum, Thread, Post
from ..models.announcement import Announcement
from ..models.menu import ClassroomMenuItem

import factory

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