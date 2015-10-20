# coding: utf-8

"""
Courseevents are for sale. This app handles the public data
of coruseevents
"""

from __future__ import unicode_literals, absolute_import

from django.db import models

from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel

from apps_productdata.mentoki_product.models.courseproduct import CourseProduct
from apps_data.course.models.course import Course

from froala_editor.fields import FroalaField

import logging
logger = logging.getLogger(__name__)


class SpecialOfferManager(models.Manager):
    """
    Querysets for CourseEvents
    """
    def for_new_customers_by_course(self, course):
        return self.filter(course=course, has_depedencies=False)

    def not_for_new_customers_by_course(self, course):
        return self.filter(course=course, has_depedencies=True)

class SpecialOffer(TimeStampedModel):

    name = models.CharField(max_length=200, default="25% Einführungsrabatt")

    description = FroalaField(blank=True, default="keine Begründung")

    percentage_off = models.IntegerField(default=0)

    courseproduct = models.OneToOneField(CourseProduct, blank=True, null=True)

    course = models.ForeignKey(Course, blank=True, null=True)

    objects = SpecialOfferManager()

    class Meta:
        verbose_name = _("Rabatt")
        verbose_name_plural = _("Rabatte")

    def __unicode__(self):
        return "%s: %s" % (self.courseproduct.name, self.name)
