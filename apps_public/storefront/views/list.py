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
        context['listheader'] = "Gesamtsortiment"
        return context


class ListNowView(TemplateView):
    template_name = "storefront/pages/courselist.html"
    listheader = "x"

    def get_context_data(self, **kwargs):
        """
        Courseproductgroups are shown as entry points to the special pages
        that describe all products that one teacher has to offer on a toipc.
        They correspond the Courses
        """
        context = super(ListNowView, self).get_context_data()

        # build list of course events
        context['courseproductgroups'] = CourseProductGroup.objects.book_now()
        context['listheader'] = "Jetzt buchbar"
        return context


class ListPreviewView(TemplateView):
    template_name = "storefront/pages/courselist.html"

    def get_context_data(self, **kwargs):
        """
        Courseproductgroups are shown as entry points to the special pages
        that describe all products that one teacher has to offer on a toipc.
        They correspond the Courses
        """
        context = super(ListPreviewView, self).get_context_data()

        # build list of course events
        context['courseproductgroups'] = CourseProductGroup.objects.preview()
        context['listheader'] = "Vorschau"
        return context