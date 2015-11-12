"""
Tests the paymentprocess for a user and a product that is available to him
https://developers.braintreepayments.com/reference/general/testing/python
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



class PaymentProcessTest(TestCase):
    """
    Tests the calculation of special offers for courseproducts:
    """
    @classmethod
    def setUp(self):
        pass