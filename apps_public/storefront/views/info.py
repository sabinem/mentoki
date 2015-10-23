# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404

from apps_productdata.mentoki_product.models.courseproductgroup import CourseProductGroup
from apps_productdata.mentoki_product.models.courseproduct import CourseProduct



class CourseProductGroupsListView(TemplateView):
    template_name = "storefront/pages/courselist.html"

    def get_context_data(self, **kwargs):
        """
        Events that are open for booking are shown. Also previews are shown as coming soon
        """
        context = super(CourseProductGroupsListView, self).get_context_data()

        # build list of course events
        context['courseproductgroups'] = CourseProductGroup.objects.published()

        return context


class CourseGroupMixin(object):

    def get_context_data(self, **kwargs):
        """
        gets product detail context
        """
        context = super(CourseGroupMixin, self).get_context_data()
        courseproductgroup = get_object_or_404(CourseProductGroup,slug=self.kwargs['slug'])
        context['courseproductgroup'] =courseproductgroup

        return context


class CourseGroupDetailView(
    CourseGroupMixin,
    TemplateView):
    """
    This View shows the details of a courseevents. From here you can book them, if they are
    available for booking yet.
    """
    template_name = "storefront/pages/coursegroupdetail.html"


class CourseGroupMentorsView(
    CourseGroupMixin,
    TemplateView):
    """
    This View shows the details of a courseevents. From here you can book them, if they are
    available for booking yet.
    """
    template_name = "storefront/pages/courseproductmentors.html"


class CourseGroupOfferView(
    CourseGroupMixin,
    TemplateView):
    """
    This View shows the details of a courseevents. From here you can book them, if they are
    available for booking yet.
    """
    template_name = "storefront/pages/courseproductoffer.html"

    def get_context_data(self, **kwargs):
        """
        gets product detail context
        """
        context = super(CourseGroupOfferView, self).get_context_data()
        course = context['courseproductgroup'].course
        user=self.request.user
        if user.is_authenticated() and hasattr(user, 'customer'):
            context['purchased_courseproducts'] = \
                user.customer.purchased_products(course=course)
            context['available_courseproducts'] = \
                user.customer.available_products(
                    course=course)
            context['out_of_reach_courseproducts'] = \
                user.customer.\
                    not_yet_avalable(
                    course=course)
        else:
            context['available_courseproducts'] = \
                CourseProduct.objects.for_new_customers_by_course(course=course)
            context['out_of_reach_courseproducts'] = \
                CourseProduct.objects.not_for_new_customers_by_course(course=course)
        print context
        return context

