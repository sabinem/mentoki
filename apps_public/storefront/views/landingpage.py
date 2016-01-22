# -*- coding: utf-8 -*-

"""
Listing of all Products that belong to one Course. This the actual landing page
for Selling the Courseevents
"""


from __future__ import unicode_literals

from django.views.generic import TemplateView

from braces.views import LoginRequiredMixin
from .info import CourseGroupMixin

import logging


class CourseLandingPageView(
    LoginRequiredMixin,
    CourseGroupMixin,
    TemplateView):
    """
    Detail Page where the Course topic is described
    """
    template_name = "storefront/pages/landingpage.html"

class CourseOfferPageView(
    LoginRequiredMixin,
    CourseGroupMixin,
    TemplateView):
    """
    Detail Page where the Course topic is described
    """
    template_name = "storefront/pages/offer.html"
