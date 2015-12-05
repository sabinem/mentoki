# -*- coding: utf-8 -*-

"""
Infopages of one CourseProductGroup corresponding to Course

There are two info pages: one describes the Course topic and what the teachers
want to teach their students in general terms.
"""

from __future__ import unicode_literals

from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404

from apps_productdata.mentoki_product.models.courseproductgroup \
    import CourseProductGroup, CourseProductGroupField


from apps_productdata.mentoki_product.models.courseproduct import CourseProduct
from apps_customerdata.customer.models.order import Order
from apps_productdata.mentoki_product.constants import ProductToCustomer



import logging
logger = logging.getLogger('public.offerpages')
logger_sentry = logging.getLogger('sentry.offerpages')



class CourseGroupMixin(object):
    """
    This mixin gets the CourseProductGroup data from the slug
    """
    def get_context_data(self, **kwargs):
        """
        adds CourseProductGroup to the request context
        """
        context = super(CourseGroupMixin, self).get_context_data()
        courseproductgroup = get_object_or_404(CourseProductGroup,slug=self.kwargs['slug'])
        context['courseproductgroup'] =courseproductgroup

        return context


class CourseGroupDetailView(
    CourseGroupMixin,
    TemplateView):
    """
    Deteil Page where the Course topic is described
    """
    template_name = "storefront/pages/coursegroupdetail.html"

    def get_context_data(self, **kwargs):
        """
        gets product detail context
        """
        context = super(CourseGroupDetailView, self).get_context_data()
        course = context['courseproductgroup'].course
        user=self.request.user
        courseproductgroup = context['courseproductgroup']
        logger.debug('Jemand sieht sich die Angebotsseite für den Kurs [%s] an.' %
                    course)

        product_fields = CourseProductGroupField.objects.fields_for_courseproduct(
            courseproductgroup = courseproductgroup
        )

        context['product_fields'] = product_fields



        # for customers: get past orders

        if hasattr(user, 'customer'):
            customer=user.customer
            logger.debug('Es geht um einen Kunden [%s]' % customer)

            ordered_products = \
                Order.objects.products_with_order_for_course_and_customer(
                    customer=customer,
                    course=course)
            logger.debug('Der Kunde hat bereits Aufträge')
        else:
            customer=None
            ordered_products=None
            logger.debug('Zu diesem Thema hat der Kunde noch nichts gebucht.')

        # get all courseproducts

        courseproducts = \
            CourseProduct.objects.\
                all_by_course_ordered_by_display_nr(course=course)
        context['courseproducts'] = courseproducts
        context['ProductToCustomer'] = ProductToCustomer

        logger.debug('Alle Kursprodukte geladen')

        product_list = []

        # decide on status of products in relation to the customer

        for courseproduct in courseproducts:

            # prepare dictionary for displaying the item
            item = {
                'courseproduct': courseproduct
            }

            logger.info('Setup zum Produkt:[%s] wird geprüft' %
             (courseproduct))

            order = courseproduct.get_order_object_for_customer(
                customer=customer)
            item['order'] = order
            logger.info(' - Es gibt einen Auftrag:[%s] für '
                        'diesen Kunden zu diesem Produkt' %
                         (order))

            # initialize flags
            item['payment_complete'] = False
            item['payment_started'] = False
            item['can_buy'] = False
            item['has_parts'] = courseproduct.can_be_bought_in_parts
            item['buy_part_nr'] = 1
            item['prebook'] = courseproduct.prebook

            if courseproduct.prebook and not courseproduct.ready_for_sale:

                logger.info('Das Produkt kann nur vorgebucht werden.')

            else:


                if order and order.started_to_pay:
                    item['payment_started'] = True
                    logger.info(' - Es gibt einen Auftrag und es wurde bereits '
                                'begonnen zu zahlen.')

                    if order.fully_paid:
                        item['payment_complete'] = True
                        logger.info(' - Der Auftrag wurde komplett bezahlt')
                    else:

                        # es gibt noch was zu zahlen

                        if courseproduct.can_be_bought_in_parts:
                            logger.info(' - Der Auftrag kann in Teilen bezahlt werden')

                            logger.info('... Bezahlung vorbereiten ...')
                            item['can_buy'] = True
                            item['has_parts'] = True
                            item['buy_part_nr'] = order.nr_parts_paid + 1
                        else:
                            logger_sentry.error(' - Produkt ist nicht vollständig bezahlt, '
                                             'aber kann nicht teilbezahlt werden.'
                                                'Auftrag: [%s]' % (order)
                                                )

                else:

                    # no order for this product exists yet or payment on the
                    # order has not started yet

                    logger.info(' - Es gibt noch keinen Auftrag, bei dem '
                                'begonnen wurde zu zahlen für dieses Produkt')
                    # check for similar products, that have been ordered
                    if not courseproduct.flag_similar_products_ordered(
                    ordered_products=ordered_products):
                        logger.info(' - Es wurden noch keine Produkte aus der selben'
                        ' Untergruppe gekauft')
                        item['can_buy'] = True

                # calculate price

                if courseproduct.price != courseproduct.sales_price:
                    item['is_on_sale'] = True
                else:
                    item['is_on_sale'] = False
                item['amount_original'] = courseproduct.price
                item['amount_sale'] = courseproduct.sales_price

                logger.info(' - item, das angezeigt wird für dieses Produkt:'
                            '(versteckte Felder [can_buy: %s, '
                            'has_parts: %s, buy_part_nr: %s, '
                            'payment_complete: %s, payment_started: %s]'
                               % (
                            item['can_buy'], item['has_parts'],
                            item['buy_part_nr'], item['payment_complete'],
                            item['payment_started']
                            ))

            product_list.append(item)

        context['product_list'] = product_list

        return context


class CourseGroupMentorsView(
    CourseGroupMixin,
    TemplateView):
    """
    Teachers Page, where the Course teachers introduce themselves
    """
    template_name = "storefront/pages/courseproductmentors.html"


