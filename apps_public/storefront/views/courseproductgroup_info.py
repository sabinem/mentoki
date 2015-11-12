# -*- coding: utf-8 -*-

"""
Infopages of one CourseProductGroup corresponding to Course

There are two info pages: one describes the Course topic and what the teachers
want to teach their students in general terms.
"""

from __future__ import unicode_literals

from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404

from apps_productdata.mentoki_product.models.courseproductgroup \
    import CourseProductGroup


class CourseGroupMixin(object):
    """
    This mixin gets the CourseProductGroup data from the slug
    """
    def get_context_data(self, **kwargs):
        """
        adds CourseProductGroup to the request context
        """
        context = super(CourseGroupMixin, self).get_context_data()
        courseproductgroup = get_object_or_404(CourseProductGroup,slug=self.kwargs['slug'])
        context['courseproductgroup'] =courseproductgroup

        return context


class CourseGroupDetailView(
    CourseGroupMixin,
    TemplateView):
    """
    Deteil Page where the Course topic is described
    """
    template_name = "storefront/pages/coursegroupdetail.html"


class CourseGroupMentorsView(
    CourseGroupMixin,
    TemplateView):
    """
    Teachers Page, where the Course teachers introduce themselves
    """
    template_name = "storefront/pages/courseproductmentors.html"


