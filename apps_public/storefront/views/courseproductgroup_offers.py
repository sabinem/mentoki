# -*- coding: utf-8 -*-

"""
Listing of CourseProductGroups corresponding to Course

CourseProductGroup is the collection of all products that
belong to one Course
"""

from __future__ import unicode_literals

from django.views.generic import TemplateView

from apps_productdata.mentoki_product.models.courseproduct import CourseProduct
from apps_customerdata.customer.models.order import Order
from apps_productdata.mentoki_product.constants import ProductToCustomer

from .courseproductgroup_info import CourseGroupMixin

import logging
logger = logging.getLogger('activity.users')


class CourseGroupOfferView(
    CourseGroupMixin,
    TemplateView):
    """
    This View shows all products that are available for a course
    """
    template_name = "storefront/pages/courseproductoffer.html"

    def get_context_data(self, **kwargs):
        """
        lists all offers for a courseproductgroup
        """
        context = super(CourseGroupOfferView, self).get_context_data()

        # the mixin already provides the courseproductgroup

        course = context['courseproductgroup'].course
        user=self.request.user
        logger.info('Jemand sieht sich die Angebotsseite für den Kurs [%s] an.' %
                    course)

        # if the user is a customer he might have past orders

        if hasattr(user, 'customer'):
            customer=user.customer
            logger.debug('Es geht um einen Kunden [%s]' % customer)
            ordered_products = \
                Order.objects.\
                products_with_order_paid_for_course_and_customer(
                    course=course,
                    customer=user.customer)
            logger.info('Der Kunde hat schon Kurse bei uns gebucht zu diesem '
                         'Thema. [%s]')
        else:
            ordered_products=None
            logger.info('Zu diesem Thema hat der Kunde noch nichts gebucht.')

        # determine availabilty of products
        courseproducts = \
            CourseProduct.objects.\
                all_by_course(course=course)



        logger.debug('Kursprodukte der Gruppe aus der Datenbank geholt.')
        product_list = []

        for courseproduct in courseproducts:

            logger.debug('Kursprodukt [%s]' % courseproduct)
            logger.debug('  - Hat Abhängigkeit [product %s]' % courseproduct.dependency)
            logger.debug('  - ist Teil von [product %s]' % courseproduct.part_of)

            if ordered_products and courseproduct in ordered_products:
                logger.debug('  - schon gebucht')
                status = ProductToCustomer.BOOKED
            elif courseproduct.available_with_past_orders(ordered_products):
                logger.debug('  - jetzt buchbar')
                status = ProductToCustomer.AVAILABLE
            else:
                logger.debug('  - jetzt nicht buchbar')
                status = ProductToCustomer.NOT_AVAILABLE
            logger.debug('  - status [%s]' % status)

            item = {
                'courseproduct': courseproduct,
                'status': status,
            }
            product_list.append(item)
        context['product_list'] = product_list
        context['ProductToCustomer'] = ProductToCustomer
        return context

