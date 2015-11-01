# -*- coding: utf-8 -*-

"""
Listing of CourseProductGroups corresponding to Course

CourseProductGroup is the collection of all products that
belong to one Course
"""

from __future__ import unicode_literals

from django.views.generic import TemplateView

from apps_productdata.mentoki_product.models.courseproductgroup import CourseProductGroup



class CourseProductGroupsListView(TemplateView):
    template_name = "storefront/pages/courselist.html"

    def get_context_data(self, **kwargs):
        """
        Courseproductgroups are shown as entry points to the special pages
        that describe all products that one teacher has to offer on a toipc.
        They correspond the Courses
        """
        context = super(CourseProductGroupsListView, self).get_context_data()

        # build list of course events
        context['courseproductgroups'] = CourseProductGroup.objects.published()

        return context




