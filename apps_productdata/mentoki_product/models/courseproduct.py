# coding: utf-8

"""
Here are the models for courseproducts, that are products that belong
to one course.
"""

from __future__ import unicode_literals, absolute_import

from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps_data.courseevent.models.courseevent import CourseEvent
from apps_data.course.models.course import Course

from .product import Product
from .courseproductgroup import CourseProductGroup, CourseProductSubGroup
from ..constants import ProductToCustomer

import logging
logger = logging.getLogger('products.courseproduct')


class CourseProductManager(models.Manager):
    """
    Querysets for CourseProducts
    """
    def all_by_course(self, course):
        """
        gets all courseproducts that have dependencies for one course
        """
        return self.filter(
            course=course)\
            .order_by('display_nr')


class CourseProduct(Product):
    """
    Course Products are Products that belong to one Course
    """
    course = models.ForeignKey(Course)
    courseproductgroup = models.ForeignKey(
        CourseProductGroup, default=1)
    #courseproductsubgroup = models.ForeignKey(
    #    CourseProductSubGroup, default=1)

    courseevent = models.ForeignKey(CourseEvent, blank=True, null=True)
    dependency = models.ForeignKey('self', null=True, blank=True, related_name="dependent_on")
    part_of = models.ForeignKey('self', null=True, blank=True, related_name="belongs_to")

    objects = CourseProductManager()

    class Meta:
        verbose_name = _("Kursprodukt")
        verbose_name_plural = _("Kursprodukte")

    def __unicode__(self):
        return u'[%s] %s' % (self.id, self.name)

    @property
    def sales_price(self):
        logger.debug('------------ calculating sales_price for [%s]'
                 % (self))
        from .specialoffer import SpecialOffer
        specialoffer = SpecialOffer.objects.get_special_offer_courseproduct(
            courseproduct=self)
        if specialoffer:
            logger.debug('specialoffer %s found for %s'
                     % (specialoffer, self))
            percentage = 100 - specialoffer.percentage_off
            logger.debug('----- percentage %s, percentage_off %s'
                     % (percentage, specialoffer.percentage_off))
            sales_price = int(self.price) * percentage / 100.00
            logger.debug('----- price %s, sales_price %s'
                     % (self.price, sales_price))
            return sales_price
        else:
            logger.debug('no specialoffer found for %s'
                     % (self))
            return self.price

    def available_with_past_orders(self, ordered_products=None):
        """
        checks for a given courseproduct and course whether it can be
        booked by a customer
        return ProductToCustomerStatus
        """
        # if no products have been orded then the product is available
        # if it has no dependencies
        if not ordered_products:
            if self.dependency:
                return ProductToCustomer.NOT_AVAILABLE
        else:
        # case ordered products exists
            if self in ordered_products:
                # product has been already ordered
                return ProductToCustomer.NOT_AVAILABLE
            else:
                if self.dependency and not self.dependency in ordered_products:
                    # dependencies are not fullfilled
                    return ProductToCustomer.NOT_AVAILABLE
                for item in ordered_products:
                    if item.part_of == self:
                        # if parts of the products have been bought already
                        return ProductToCustomer.NOT_AVAILABLE
                if self.part_of in ordered_products:
                    # the whole of which the product is a part of has already
                    # been bought
                    return ProductToCustomer.NOT_AVAILABLE
        return ProductToCustomer.AVAILABLE

