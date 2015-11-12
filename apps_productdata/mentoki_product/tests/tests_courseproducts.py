"""
Tests Price calculation with Specialoffer

"""

# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.core.validators import ValidationError

from django.test import TestCase

from apps_productdata.mentoki_product.models.specialoffer import SpecialOffer
from apps_productdata.mentoki_product.constants import Offerreach, Currency
from apps_productdata.mentoki_product.models.courseproduct import CourseProduct

from tests.factories import CourseFactory, \
    CourseProductFactory, SpecialOfferFactory


class CourseproductAndSpecialOfferTest(TestCase):
    """
    Tests the calculation of special offers for courseproducts:
    """
    @classmethod
    def setUp(self):
        pass
        # create courses
        # TODO Setup: what is needed
        # courses
        # courseevents
        # courseproducts
        # user
        # customer
        # order

    def test_case_user_not_yet_customer(self):
        """
        only products without depencies ahould be available
        """
        pass

    def test_case_customer_no_orders(self):
        """
        same as above
        """
        pass

    def test_case_customer_part_orders(self):
        """
        next partt should be available, the corresponding whole
        course should not be available
        """
        pass

    def test_case_customer_complete_courseevent_order(self):
        """
        tests whether all products for a course are found
        """
