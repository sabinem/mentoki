# coding: utf-8


"""
Courseevents are for sale. This app handles the public data
of coruseevents
"""

from __future__ import unicode_literals, absolute_import

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel
from model_utils import Choices

from apps_productdata.mentoki_product.models.courseproduct import CourseProduct
from apps_customerdata.customer.models.customer import Customer
from django.conf import settings
from apps_customerdata.customer.models.transaction import Transaction


import logging
logger = logging.getLogger(__name__)


class TempOrderManager(models.Manager):
    """
    Manager for attempted orders
    """
    def create(
            self,
            courseproduct,
            by_authenticated_user,
            for_self,
            user=None,
            participant_first_name=None,
            participant_last_name=None,
            participant_username=None,
            participant_email=None):
        temporder = TempOrder(
            courseproduct=courseproduct,
            by_authenticated_user=by_authenticated_user,
            for_self=for_self,
            user=user,
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
    by_authenticated_user = models.BooleanField(default=False)
    for_self = models.BooleanField(default=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='Teilnehmer als Benutzer',
        default=1,
        blank=True,
        null=True
    )
    participant_email=models.EmailField(
        verbose_name='Email des Teilnehmers',
        blank=True,
    )
    participant_first_name = models.CharField(max_length=40, blank=True)
    participant_last_name = models.CharField(max_length=40, blank=True)
    participant_username = models.CharField(max_length=40, blank=True)

    objects = TempOrderManager()
