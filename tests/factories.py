# coding: utf-8

from __future__ import unicode_literals, absolute_import

import factory

from apps_data.course.models.course import Course
from django.contrib.sites.models import Site

from apps_data.courseevent.models.courseevent import CourseEvent,\
    CourseEventParticipation
from apps_data.courseevent.models.forum import Forum, Thread, Post
from apps_data.courseevent.models.announcement import Announcement
from apps_productdata.mentoki_product.models.courseproduct import \
    CourseProduct
from apps_productdata.mentoki_product.models.specialoffer import \
    SpecialOffer


class CourseFactory(factory.DjangoModelFactory):
    class Meta:
        model = Course


class SiteFactory(factory.DjangoModelFactory):
    class Meta:
        model = Site


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


class CourseProductFactory(factory.DjangoModelFactory):
    class Meta:
        model = CourseProduct


class SpecialOfferFactory(factory.DjangoModelFactory):
    class Meta:
        model = SpecialOffer