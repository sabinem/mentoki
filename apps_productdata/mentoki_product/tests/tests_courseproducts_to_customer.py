"""
Tests for Products to Customer:
depending on past orders products may or may not be available to customers
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
        # create courses
        self.course_1 = CourseFactory.create(slug="slug1")
        self.course_2 = CourseFactory.create(slug="slug2")
        self.course_3 = CourseFactory.create(slug="slug3")

        self.user

        # a product for course 1: one offer there
        self.product_a_1 = CourseProductFactory.create(
            course=self.course_1,
            price=10.00,
            currency=Currency.EUR)
        # a product for course 3: no offer there
        self.product_b_2 = CourseProductFactory.create(
            course=self.course_2,
            price=10.00,
            currency=Currency.EUR)
        # a product for course 3: no offer there
        self.product_c_3 = CourseProductFactory.create(
            course=self.course_3,
            price=100.00,
            currency=Currency.EUR)
        self.offer_1 = SpecialOfferFactory.create(
            course=self.course_1,
            percentage_off=25,
            offerreach=Offerreach.COURSE)
        # an offer for course 2 75% off
        self.offer_3 = SpecialOfferFactory.create(
            course=self.course_3,
            percentage_off=75,
            offerreach=Offerreach.COURSE)

    def test_whether_right_offer_is_found_and_applied_to_product(self):
        """
        tests whher the sales price is calculated right taking the
        offers into account
        """
        self.assertEqual(self.product_a_1.sales_price,7.50)
        self.assertEqual(self.product_c_3.sales_price,25.00)

    def test_case_no_offer_exists(self):
        """
        if no offer is found the sales price should be identical to the
        product price
        """
        SpecialOffer.objects.get_special_offer_courseproduct(
            self.product_b_2) # no offer exist
        self.assertEqual(self.product_b_2.sales_price,10.00)

    def test_that_no_contradictional_offers_are_allowed(self):
        """
        there should not be to offers with reach course that contradict
        each other.
        """
        offer_3 = SpecialOffer(
            course=self.course_1,
            percentage_off=35,
            offerreach=Offerreach.COURSE)
        self.assertRaises(ValidationError, offer_3.clean)

    def test_all_products_for_course_should_be_found(self):
        """
        tests whether all products for a course are found
        """
        courseproducts1 = CourseProduct.objects.all_by_course(
            course=self.course_1)
        courseproducts2 = CourseProduct.objects.all_by_course(
            course=self.course_2)
        courseproducts3 = CourseProduct.objects.all_by_course(
            course=self.course_3)
        self.assertQuerysetEqual(
            courseproducts1,
            [repr(self.product_a_1)],
            ordered=False)
        self.assertQuerysetEqual(
            courseproducts1,
            [repr(self.product_b_2)])
        self.assertQuerysetEqual(
            courseproducts3,
            [repr(self.product_c_3)])