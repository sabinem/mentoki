# -*- coding: utf-8 -*-

"""
Listing of CourseProductGroups corresponding to Course

CourseProductGroup is the collection of all products that
belong to one Course
"""

from __future__ import unicode_literals

from django.views.generic import TemplateView

from apps_productdata.mentoki_product.models.courseproduct import CourseProduct
from apps_productdata.mentoki_product.constants import PRODUCT_TO_CUSTOMER_CASES
from apps_customerdata.customer.models.order import Order
from apps_data.courseevent.models.courseevent import CourseEventParticipation
from apps_data.courseevent.constants import PARTICIPANT_STATUS_CHOICES

from .courseproductgroup_info import CourseGroupMixin

import logging
#logger = logging.getLogger('public.customers')
logger = logging.getLogger(__name__)

class CourseGroupOfferView(
    CourseGroupMixin,
    TemplateView):
    """
    This View shows all products that are available for a course
    """
    template_name = "storefront/pages/courseproductoffer.html"

    def get_context_data(self, **kwargs):
        """
        gets product detail context
        """
        context = super(CourseGroupOfferView, self).get_context_data()
        course = context['courseproductgroup'].course
        user=self.request.user
        logger.info('offerpage view for course [%s]' % course)

        # -------------------------------------------------------------
        # determine whether user is customers and whether orders exist
        # -------------------------------------------------------------
        if hasattr(user, 'customer'):
            customer=user.customer
            logger.debug('1. user is a customer [%s]' % customer)
            ordered_products = \
                Order.objects.\
                products_with_order_paid_for_course_and_customer(
                    course=course,
                    customer=user.customer)
            logger.debug('- has already ordered products')
        else:
            ordered_products=None
            logger.debug('1. user is not a customer')

        # -------------------------------------------------------------
        # determine availablity of products for the user
        # -------------------------------------------------------------
        courseproducts = \
            CourseProduct.objects.\
                all_by_course(course=course)
        logger.debug('2. fetched all courseproducts')
        product_list = []

        for courseproduct in courseproducts:

            logger.debug('- considering product [%s]' % courseproduct)
            logger.debug('  - has dependency [product %s]' % courseproduct.dependency)
            logger.debug('  - is part of [product %s]' % courseproduct.part_of)

            if ordered_products and courseproduct in ordered_products:
                logger.debug('  - schon gebucht')
                status = 'booked'
            elif courseproduct.available_with_past_orders(ordered_products):
                logger.debug('  - jetzt buchbar')
                status = 'available'
            else:
                logger.debug('  - jetzt nicht buchbar')
                status = 'not_available'
            logger.debug('  - status [%s]' % status)

            item = {
                'courseproduct': courseproduct,
                'status': status,
            }
            product_list.append(item)
        context['product_list'] = product_list
        return context

