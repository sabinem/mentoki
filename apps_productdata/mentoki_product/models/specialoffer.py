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
from django_enumfield import enum
from ..constants import Offerreach

import logging
logger = logging.getLogger('__name__')


class SpecialOfferManager(models.Manager):
    """
    Querysets for courseoffers
    """
    def get_special_offer_courseproduct(self, courseproduct):
        """
        This function searches for the offer that applies to a courseproduct.

        So far there is only one reach for an offer: that of the course

        :param courseproduct:
        :return: offer or None, if no offer exists
        """
        logger.debug('Suche nach Rabatt für Produkt: [%s]'
             % (courseproduct))
        try:
            offer = self.get(
                course=courseproduct.course,
                offerreach=Offerreach.COURSE)
            logger.debug('Kursgruppenangebot [%s] gefunden für Kursgruppe: [%s]'
                        ', [%s] Prozent Rabatt'
                     % (offer, offer.course, offer.percentage_off))
            return offer
        except ObjectDoesNotExist:
            logger.debug('Es gibt keinen Rabatt für dieses Produkt.')
            return None

    def count_course_offers_per_course(self, course):
        return self.filter(course=course, offerreach=Offerreach.COURSE).count()



class SpecialOffer(TimeStampedModel):

    course = models.ForeignKey(Course, blank=True, null=True)

    name = models.CharField(max_length=200, default="25% Einführungsrabatt")
    description = FroalaField(blank=True, default="zur Einführung")

    percentage_off = models.IntegerField(default=0)
    offerreach = enum.EnumField(Offerreach, default=Offerreach.COURSE)

    objects = SpecialOfferManager()

    class Meta:
        verbose_name = _("Rabatt")
        verbose_name_plural = _("Rabatte")

    def __unicode__(self):
        return "%s: %s" % (self.name, self.offerreach)

    def clean(self, **kwargs):
        if self.offerreach == Offerreach.COURSE:
            if not self.id: #insert
                if SpecialOffer.objects.count_course_offers_per_course(
                    course=self.course) > 0:
                    raise ValidationError('Nur ein kursweiter Rabatt pro'
                                          ' Kurs ist erlaubt.')
