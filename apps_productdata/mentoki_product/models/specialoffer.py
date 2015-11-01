# coding: utf-8

"""
Courseevents are for sale. This app handles the public data
of coruseevents
"""

from __future__ import unicode_literals, absolute_import

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ObjectDoesNotExist

from model_utils.models import TimeStampedModel
from froala_editor.fields import FroalaField

from apps_productdata.mentoki_product.models.courseproduct import CourseProduct
from apps_data.course.models.course import Course
from apps_data.courseevent.models.courseevent import CourseEvent
from ..constants import OFFERREACH_CHOICES
from apps_productdata.mentoki_product.models.producttype import ProductType

import logging
logger = logging.getLogger(__name__)


class SpecialOfferManager(models.Manager):
    """
    Querysets for CourseEvents
    """
    def get_special_offer_courseproduct(self, courseproduct):
        logger.debug('searching for offer for %s'
             % (courseproduct))
        try:
            logger.debug('try productoffers')
            offer = self.get(
                courseproduct=courseproduct,
                reach=OFFERREACH_CHOICES.product)
            logger.debug('productoffer found: %s'
                     % (offer))
            return offer
        except ObjectDoesNotExist:
            pass # try next filter
        """
        if courseproduct.product_type.is_courseevent_participation:
            logger.debug('try eventoffers')
            try:
                offer = self.get(
                    courseevent=courseproduct.courseevent,
                    reach=OFFERREACH_CHOICES.courseevent)
                logger.debug('eventoffer found: %s'
                     % (offer))
                return offer
            except ObjectDoesNotExist:
                pass # try next filter
        try:
            logger.debug('try courseoffers')
            offer = self.get(
                course=courseproduct.course,
                reach=OFFERREACH_CHOICES.course)
            logger.debug('courseoffer found: %s'
                 % (offer))
            return offer
        except ObjectDoesNotExist:
            return None
        """


class SpecialOffer(TimeStampedModel):

    name = models.CharField(max_length=200, default="25% Einführungsrabatt")
    description = FroalaField(blank=True, default="zur Einführung")

    percentage_off = models.IntegerField(default=0)

    courseproduct = models.OneToOneField(CourseProduct, blank=True, null=True)
    courseevent = models.ForeignKey(CourseEvent, blank=True, null=True)
    course = models.ForeignKey(Course, blank=True, null=True)

    reach=models.CharField(
        max_length=10,
        choices=OFFERREACH_CHOICES,
        default=OFFERREACH_CHOICES.course)

    objects = SpecialOfferManager()

    class Meta:
        verbose_name = _("Rabatt")
        verbose_name_plural = _("Rabatte")

    def __unicode__(self):
        return "%s: %s" % (self.name, self.reach)
