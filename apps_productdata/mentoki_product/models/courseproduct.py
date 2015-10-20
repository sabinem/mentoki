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

import logging
logger = logging.getLogger(__name__)


class CourseProductManager(models.Manager):
    """
    Querysets for CourseEvents
    """
    def for_new_customers_by_course(self, course):
        return self.filter(course=course, has_depedencies=False).order_by('display_nr')

    def not_for_new_customers_by_course(self, course):
        return self.filter(course=course, has_depedencies=True).order_by('display_nr')

class CourseProduct(TimeStampedModel):

    name = models.CharField(max_length=200, default="Kurs-Teilnahme")

    description = FroalaField()

    product_nr = models.CharField(max_length=20, default=1)

    slug = models.SlugField()

    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name=_('Verkaufspreis'))

    display_nr = models.IntegerField(default=1)

    price_changed = MonitorField(
            monitor='price',
            verbose_name=_("letzte Preisänderung am"))
    CURRENCY_CHOICES = Choices(
        ('EUR', 'euro',_('Euro')),
        ('CHF', 'chf',_('Schweizer Franken')),
    )
    currency = models.CharField( max_length=3, choices=CURRENCY_CHOICES,
                                 default=CURRENCY_CHOICES.euro )

    can_be_bought_only_once = models.BooleanField(default=False)
    has_depedencies = models.BooleanField(default=False)
    dependencies = models.ForeignKey('self', null=True, blank=True)
    course = models.ForeignKey(Course)
    courseevent = models.ForeignKey(CourseEvent, blank=True, null=True)
    PRODUCT_TYPE = Choices(('courseevent', 'courseevent', _('Kursteilnahme')),
                           ('part', 'courseevent_part', _('Teilabschnitt einer Kurses')),
                           ('addon', 'other', _('anderes Produkt')),
                           ('selflearn', 'selflearn', _('Material und Forum-Zugang')),
                           )
    product_type =  models.CharField(
        verbose_name="Produktart",
        max_length=12,
        choices=PRODUCT_TYPE,
        default=PRODUCT_TYPE.courseevent)

    objects = CourseProductManager()

    class Meta:
        verbose_name = _("Kurs-Produkt")
        verbose_name_plural = _("Kurs-Produkte")

    def __unicode__(self):
        return "%s: %s" % (self.course.title, self.name)

    @property
    def sales_price(self):
        if hasattr(self, 'specialoffer'):
            percentage = 100 - self.specialoffer.percentage_off
            print "======== percentage %s" % percentage
            sales_price = int(self.price) * percentage / 100.00
            print "--- sales_price %s -> %s" % (self.price, sales_price)
            return sales_price


    def save(self, *args, **kwargs):
        #TODO check wether prices addup to total price
        super(CourseProduct, self).save(*args, **kwargs)


class CourseAddOnProductManager(models.Manager):
    def get_queryset(self):
        return super(CourseAddOnProductManager, self).get_queryset().filter(
            product_type='addon')

class CourseEventProductPartManager(models.Manager):
    def get_queryset(self):
        return super(CourseEventProductPartManager, self).get_queryset().filter(
            product_type='part')

class CourseEventProductManager(models.Manager):
    def get_queryset(self):
        return super(CourseEventProductManager, self).get_queryset().filter(
            product_type='courseevent')


class CourseEventFullProduct(CourseProduct):
    class Meta:
        proxy = True

    def __str__(self):
        return self.name.upper()


class CourseEventPartProduct(CourseProduct):
    class Meta:
        proxy = True

    def __str__(self):
        return self.name.upper()


class CourseAddOnProduct(CourseProduct):
    class Meta:
        proxy = True

    def __str__(self):
        return self.name.upper()

