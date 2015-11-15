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
from django.core.validators import ValidationError

from model_utils.models import TimeStampedModel
from froala_editor.fields import FroalaField

from apps_data.course.models.course import Course
from apps_productdata.mentoki_product.models.courseproduct import \
    CourseProduct
from apps_productdata.mentoki_product.models.courseproductgroup import \
    CourseProductGroup, CourseProductSubGroup
from django_enumfield import enum
from ..constants import Offerreach

import logging
logger = logging.getLogger('data.productdata')


def calculate_sales_price(percentage_off, price):
    """
    Calculates the sale price from the original price and the precentage off
    value
    :param percentage_off:
    :param price:
    :return: sales price
    """
    percentage = 100 - percentage_off
    sales_price = int(price) * percentage / 100.00
    logger.info('Mit [%s] Procent off wurde aus dem Preis [%s] der '
                'Verkaufspreis [%s] berechnet'
                % (percentage_off, price, sales_price))
    return sales_price


class SpecialOfferManager(models.Manager):
    """
    Querysets for courseoffers
    """
    def apply_specialoffer_to_courseproduct(
            self,
            courseproduct,
            price):
        """
        This function searches for the offer that applies to a courseproduct.

        So far there is only one reach for an offer: that of the course

        :param courseproduct:
        :return: offer or None, if no offer exists
        """
        logger.debug('Suche nach Rabatt für Produkt: [%s], es soll auf Preis '
                     '[%s] angewendet werden.'
             % (courseproduct, price))

         # try first option: offer for courseproduct

        try:
            specialoffer = self.get(
                courseproduct=courseproduct,
                offerreach=Offerreach.PRODUCT)
            logger.debug('Einzelangebot gefunden für [%s]: [%s] Rabatt'
                     % (courseproduct, specialoffer.percentage_off))
            return calculate_sales_price(specialoffer.percentage_off, price)
        except ObjectDoesNotExist:
            pass

         # try next option: offer for courseproductsubgroup

        try:
            specialoffer = self.get(
                courseproductsubgroup=courseproduct.courseproductsubgroup,
                offerreach=Offerreach.PRODUCTSUBGROUP)
            logger.debug('Untergruppenangebot gefunden für [%s]: [%s] Rabatt'
                     % (courseproduct.courseproductsubgroup,
                        specialoffer.percentage_off))
            return calculate_sales_price(specialoffer.percentage_off, price)
        except ObjectDoesNotExist:
            pass

        # try next option: offer for courseproductgroup

        try:
            specialoffer = self.get(
                courseproductgroup=courseproduct.courseproductgroup,
                offerreach=Offerreach.PRODUCTGROUP)
            logger.debug('Gruppenangebot gefunden für [%s]: [%s] Rabatt'
                     % (courseproduct.courseproductgroup,
                        specialoffer.percentage_off))
            return calculate_sales_price(specialoffer.percentage_off, price)
        except ObjectDoesNotExist:
            logger.debug('Es gibt keinen Rabatt für das Produkt [%s].'
                         % courseproduct)

            # return original price, if no offer was found
            return price

    def count_course_offers_per_course(self, course):
        return self.filter(course=course, offerreach=Offerreach.COURSE).count()


class SpecialOffer(TimeStampedModel):

    courseproductgroup = models.ForeignKey(CourseProductGroup, blank=True, null=True)
    courseproductsubgroup = models.ForeignKey(CourseProductSubGroup, blank=True, null=True)
    courseproduct = models.ForeignKey(CourseProduct, blank=True, null=True)
    course = models.ForeignKey(Course, blank=True, null=True)
    name = models.CharField(max_length=200, default="25% Einführungsrabatt")
    description = FroalaField(blank=True, default="zur Einführung")

    percentage_off = models.IntegerField(default=0)
    offerreach = enum.EnumField(Offerreach, default=Offerreach.PRODUCTGROUP)

    objects = SpecialOfferManager()

    class Meta:
        verbose_name = _("Rabatt")
        verbose_name_plural = _("Rabatte")

    def __unicode__(self):
        return "%s: %s" % (self.name, self.offerreach)

    def clean(self, **kwargs):
        if self.offerreach == Offerreach.PRODUCT:
            if not self.courseproduct:
                raise ValidationError(
                    'Ein Rabatt der sich auf ein Produkt '
                    'bezieht braucht ein Produkt')
            if not self.id: #insert
                #if SpecialOffer.objects.count_course_offers_per_course(
                #     course=self.course) > 1:
                #    raise ValidationError('Nur ein kursweiter Rabatt pro'
                #                          ' Kurs ist erlaubt.')
                pass
        #TODO: clean vervollständigen: genau ein ANgebot auf jeder Ebene möglich