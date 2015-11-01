# coding: utf-8


"""
Courseevents are for sale. This app handles the public data
of coruseevents
"""

from __future__ import unicode_literals, absolute_import

from django.db import models

from model_utils.models import TimeStampedModel

from apps_productdata.mentoki_product.models.courseproduct import CourseProduct

from django.conf import settings


import logging
logger = logging.getLogger(__name__)


class TempOrderManager(models.Manager):
    """
    Manager for attempted orders
    """
    def create(
            self,
            courseproduct,
            user=None,
            participant_first_name="",
            participant_last_name="",
            participant_username="",
            participant_email=None):
        if user.is_authenticated():
            temporder = TempOrder(
                courseproduct=courseproduct,
                user=user)
        else:
            temporder = TempOrder(
                courseproduct=courseproduct,
                participant_email=participant_email,
                participant_first_name=participant_first_name,
                participant_last_name=participant_last_name,
                participant_username=participant_username
            )
        temporder.save()
        return temporder


class TempOrder(TimeStampedModel):
    """
    Attempted Order is already registered, but not mixed with the valid orders
    """
    courseproduct = models.ForeignKey(CourseProduct, blank=True, null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='Teilnehmer als Benutzer',
        blank=True,
        null=True
    )
    participant_email=models.EmailField(
        verbose_name='Email des Teilnehmers',
        blank=True, null=True
    )
    participant_first_name = models.CharField(
        max_length=40, blank=True)
    participant_last_name = models.CharField(max_length=40, blank=True)
    participant_username = models.CharField(max_length=40, blank=True)

    objects = TempOrderManager()
