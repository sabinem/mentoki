# coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.db import models

from django_enumfield import enum

from model_utils.models import TimeStampedModel

from apps_productdata.mentoki_product.models.courseproductgroup \
    import CourseProductGroup
from ..constants import ContactReason

import logging
logger = logging.getLogger(__name__)


class ContactManager(models.Manager):
    """
    Manager for contacts:
    """
    pass

class Contact(TimeStampedModel):
    """
    Contacts are stored
    """
    first_name = models.CharField(max_length=40, blank=True)
    last_name = models.CharField(max_length=40, blank=True)
    email = models.EmailField(
    )
    message = models.TextField()
    contact_reason = enum.EnumField(
        ContactReason,
        default=ContactReason.LEARN
    )

    class Meta:
        verbose_name = 'Kontakte'
        verbose_name_plural = 'Kontakte'

    objects = ContactManager()

    def __unicode__(self):
        return '%s' % (self.email)


class Prebooking(TimeStampedModel):
    """
    Prebooking for Courses
    """
    name = models.CharField(
        verbose_name="Name",
        max_length=80, blank=True)
    email = models.EmailField(
        verbose_name="Email"
    )
    interested_in_learning = models.ForeignKey(
        CourseProductGroup,
        verbose_name="Kurs",
    )
    message = models.TextField(
        verbose_name="Ihre Nachricht"
    )

    class Meta:
        verbose_name = 'Voranmeldung'
        verbose_name_plural = 'Voranmeldung'
        unique_together = (('email', 'interested_in_learning'),)

    objects = ContactManager()

    def __unicode__(self):
        return '%s' % (self.email)