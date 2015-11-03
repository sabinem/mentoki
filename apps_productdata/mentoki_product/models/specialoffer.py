# coding: utf-8

"""
This module stores special offer for courseevents. These offers are
always in the form: percentage off the regular price.
They have differnt reach: they can be valid for a course, a courseevent or a
product. The offer is taken from the more specialisied to the less specialized.
So if an offer for a product exists, that one has priority over an offer that
is valid for the course.
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

import logging
logger = logging.getLogger('__name__')


class SpecialOfferManager(models.Manager):
    """
    Querysets for courseoffers
    """
    def get_special_offer_courseproduct(self, courseproduct):
        """
        This function searches for the offer that applies to a courseproduct
        :param courseproduct:
        :return: offer or None, if no offer exists
        """
        logger.debug('Suche nach Rabatt für Produkt: [%s]'
             % (courseproduct))
        try:
            offer = self.get(
                courseproduct=courseproduct,
                reach=OFFERREACH_CHOICES.product)
            logger.debug('Produktangebot [%s] gefunden für Produkt: [%s], '
                        '[%s] Prozent Rabatt'
                     % (offer, offer.coursproduct, offer.percentage_off))
            return offer
        except ObjectDoesNotExist:
            pass # try next filter

        if courseproduct.product_type \
                and courseproduct.product_type.is_courseevent_participation:
            try:
                offer = self.get(
                    courseevent=courseproduct.courseevent,
                    reach=OFFERREACH_CHOICES.courseevent)
                logger.debug('Kursangebot gefunden: [%s] für Kurs: [%s], '
                            '[%s] Prozent Rabatt'
                            % (offer, offer.courseevent, offer.percentage_off))
                return offer
            except ObjectDoesNotExist:
                pass # try next filter
        try:
            offer = self.get(
                course=courseproduct.course,
                reach=OFFERREACH_CHOICES.course)
            logger.debug('Kursgruppenangebot [%s] gefunden für Kursgruppe: [%s]'
                        ', [%s] Prozent Rabatt'
                     % (offer, offer.course, offer.percentage_off))
            return offer
        except ObjectDoesNotExist:
            logger.debug('Es gibt keinen Rabatt für dieses Produkt.')
            return None



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
