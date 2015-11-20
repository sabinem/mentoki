# coding: utf-8

"""
Here are the models for courseproducts, that are products that belong
to one course.
"""

from __future__ import unicode_literals, absolute_import

from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import ugettext_lazy as _

from apps_data.courseevent.models.courseevent import CourseEvent
from apps_data.course.models.course import Course

from .product import Product
from .courseproductgroup import CourseProductGroup, CourseProductSubGroup
from ..constants import ProductToCustomer

import logging
logger = logging.getLogger('data.productdata')


class CourseProductManager(models.Manager):
    """
    Querysets for CourseProducts
    """
    def all_by_course_ordered_by_display_nr(self, course):
        """
        gets all courseproducts that have dependencies for one course
        """
        return self\
            .filter(
                course=course,
                published=True)\
            .order_by('display_nr')

    def ordered_subgroups(self, ordered_products):
        if ordered_products:
            return self.filter(id__in=ordered_products).\
                values_list('courseproductsubgroup', flat=True)
        return []

class CourseProduct(Product):
    """
    Course Products are Products that belong to one Course
    """
    courseevent = models.ForeignKey(CourseEvent, blank=True, null=True)
    name = models.CharField(max_length=200, default="Kurs-Teilnahme")

    course = models.ForeignKey(Course)
    courseproductgroup = models.ForeignKey(
        CourseProductGroup, default=1)
    courseproductsubgroup = models.ForeignKey(
        CourseProductSubGroup, default=1)

    prebook = models.BooleanField(
        default=False
    )
    ready_for_sale = models.BooleanField(
        default=False
    )
    published = models.BooleanField(
        default=False
    )
    can_be_bought_in_parts = models.BooleanField(default=False)
    nr_parts = models.IntegerField(
        default=1
    )

    objects = CourseProductManager()

    class Meta:
        verbose_name = _("Kursprodukt")
        verbose_name_plural = _("Kursprodukte")
        unique_together = ('courseevent', 'name')

    def __unicode__(self):
        return u'%s' % (self.name)

    @property
    def sales_price(self):
        from .specialoffer import SpecialOffer
        return SpecialOffer.objects.apply_specialoffer_to_courseproduct(
            courseproduct=self, price=self.price)

    def get_order_object_for_customer(self, customer):

        logger.info('Order für Kunde und Produkt wird herausgesucht:'
                    'Produkt[%s], Kunde [%s]'
                    % (self, customer))

        try:
            from apps_customerdata.customer.models.order import Order
            logger.info('ja, gefunden')
            return Order.objects.get(courseproduct=self,
                                     customer=customer)
        except ObjectDoesNotExist:
            logger.info('nein, nichts gefunden')
            return None

    def flag_similar_products_ordered(self, ordered_products):
        ordered_subgroups = CourseProduct.objects.ordered_subgroups(
            ordered_products=ordered_products)
        logger.info('Ähnliche Produkte zu '
                    'gesucht: schon georderte Untergruppen: [%s], '
                    'eigene Untergruppe: [%s]'
                    % (ordered_subgroups,
                       self.courseproductsubgroup.id))
        if self.courseproductsubgroup.id in ordered_subgroups:
            return True
        else:
            return False

    def flag_customer_can_buy(self, ordered_products, customer):
        if self.flag_similar_products_ordered(
            ordered_products=ordered_products):
            return False
        elif self.id in ordered_products:
            from apps_customerdata.customer.constants import OrderStatus
            order = self.get_order_object_for_customer(
                ordered_products=ordered_products,
                customer=customer
            )
            if order.status == OrderStatus.FULLY_PAID:
                return False
            else:
                return True
        else:
            return True

    def next_part_nr(self, customer):
        if self.can_be_bought_in_parts:
            try:
                order = self.get_order_object_for_customer(customer=customer)
                return order.nr_parts_paid + 1
            except (ObjectDoesNotExist, AttributeError) as ex:
                return 1

