# coding: utf-8


"""
Courseevents are for sale. This app handles the public data
of coruseevents
"""

from __future__ import unicode_literals, absolute_import

from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel
from model_utils.fields import MonitorField
from model_utils import Choices

from apps_data.courseevent.models.courseevent import CourseEvent
from apps_data.course.models.course import Course

from froala_editor.fields import FroalaField

from ..constants import CURRENCY_CHOICES
from .product import Product

import logging
logger = logging.getLogger(__name__)



class CourseProductPartManager(models.Manager):
    """
    Querysets for CourseProducts
    """
    def without_dependencies_by_course(self, course):
        """
        gets all courseproducts that have no dependencies for one course
        """
        return self.filter(
            course=course,
            product_type__has_dependencies=False)\
            .order_by('display_nr')

    def with_dependencies_by_course(self, course):
        """
        gets all courseproducts that have dependencies for one course
        """
        return self.filter(
            course=course,
            product_type__has_dependencies=True)\
            .order_by('display_nr')

    def available_for_user_by_course(self, course, user):
        """
        gets all courseproducts that have dependencies for one course
        """
        return self.filter(
            course=course,
            product_type__has_dependencies=True)\
            .order_by('display_nr')


class CourseProductPart(Product):
    """
    Course Products are Products that belong to one Course
    """
    dependencies = models.ForeignKey('self', null=True, blank=True)
    course = models.ForeignKey(Course)
    courseevent = models.ForeignKey(CourseEvent, blank=True, null=True)

    objects = CourseProductPartManager()

    class Meta:
        verbose_name = _("Kursabschnitt")
        verbose_name_plural = _("Kursabschnitt")

    def __unicode__(self):
        return "%s: %s" % (self.course.title, self.name)

    @property
    def sales_price(self):
        if hasattr(self, 'specialoffer'):
            percentage = 100 - self.specialoffer.percentage_off
            sales_price = int(self.price) * percentage / 100.00
            return sales_price
        else:
            return self.price


