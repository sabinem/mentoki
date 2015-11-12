"""
Tests that only registered users with confirmed email can pay

"""

# coding: utf-8

from __future__ import unicode_literals, absolute_import

from django.core.validators import ValidationError

from django.test import TestCase, Client

from apps_productdata.mentoki_product.models.specialoffer import SpecialOffer
from apps_productdata.mentoki_product.constants import Offerreach, Currency
from apps_productdata.mentoki_product.models.courseproduct import CourseProduct



from tests.factories import CourseFactory, \
    CourseProductFactory, SpecialOfferFactory


class PaymentAuthTest(TestCase):
    """
    setup product
    setup user authenticated, but has already ordered the product
    setup anonymous user
    mock available with past orders so this function is not tested double

    """
    @classmethod
    def setUp(self):
        self.client=Client()


    def test_case_user_not_yet_customer(self):
        """
        test that anonymous user is not able to get into the view
        """
        #response = self.client.get(reverse(''))
        #self.assertRedirects(response, url)
        #response = self.client.post(url, data)
        #self.assertEqual(response.status_code,403)
        #https://docs.djangoproject.com/en/1.8/topics/testing/advanced/






    def test_case_customer_no_orders(self):
        """
        test for user whos email was not confirmed, that he is unable to enter
        the view
        """
        pass

    def test_case_customer_part_orders(self):
        """
        test customer for whom a product is not available that he is unable
        to enter
        """
        request = RequestFactory()


