"""
Tests Courses: models, updates, CourseOwner Updates,
Views and Forms

tested are the following apps and models/views:

1. apps_data.course.models.course: models Course and CourseOwner
2. apps_internal.coursebackend.views.course

"""

# coding: utf-8

from __future__ import unicode_literals, absolute_import

import unittest

from django.contrib.auth import get_user_model
from django.core.validators import ValidationError

from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from apps_productdata.mentoki_product.constants import CURRENCY_CHOICES, \
    OFFERREACH_CHOICES

from ..factories import CourseFactory, SiteFactory, \
    CourseEventFactory, CourseProductFactory

from django.test import Client

class CourseandCourseOwnerTest(TestCase):
    """
    Tests the calculation of special offers for courseproducts:
    """
    @classmethod
    def setUp(self):
        # create courses
        self.course_1 = CourseFactory.create()
        self.course_2 = CourseFactory.create()
        #create courseevents: event_i_j belongs to course j
        self.event_1_1 = CourseEventFactory.create(course=self.course1)
        self.event_2_1 = CourseEventFactory.create(course=self.course1)
        self.event_3_2 = CourseEventFactory.create(course=self.course1)
        # a product that has all attributes set
        self.product_a_2_1 = CourseEventFactory.create(
            course=self.course1,
            price=10.00,
            currency=CURRENCY_CHOICES.euro)
        # a product that has no courseevent set
        self.product_b___1 = CourseEventFactory.create(
            course=self.course1,
            courseevent=None,
            price=10.00,
            currency=CURRENCY_CHOICES.chf)
        # a product that hurts data integrity
        self.product_c_3_1 = CourseEventFactory.create(
            course=self.course1,
            courseevent=None,
            price=10.00,
            currency=CURRENCY_CHOICES.chf)
        # an offer with reach course
        self.offer____1 = CourseEventFactory.create(
            course=self.course1,
            percentage_off=25)
        # an offer with reach course
        self.offer_____2 = CourseEventFactory.create(
            course=self.course1,
            percentage_off=75,
            reach=OFFERREACH_CHOICES.course)
        # an offer with reach courseevent
        self.offer___3_2 = CourseEventFactory.create(
            course=self.course2,
            percentage_off=75,
            reach=OFFERREACH_CHOICES.courseevent)
        # an offer with reach course
        self.offer_a___2 = CourseEventFactory.create(
            course=self.course1,
            percentage_off=75)
        # an offer with reach course
        self.offer_____2 = CourseEventFactory.create(
            course=self.course1,
            percentage_off=75)

    def test_course_property_teachersrecord(self):
        """
        apps_data.course.models.course
        model: Course, method: teachersrecord
        -------------------------------------
        Teachers should be shown as a record of names
        with main teacher appearing first
        """
        self.assertEqual(self.course1.teachersrecord,
                         "firstname1 lastname1 und firstname2 lastname2")


