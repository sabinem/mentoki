# -*- coding: utf-8 -*-

from django.contrib.sitemaps import Sitemap
from django.shortcuts import render
from django.core.urlresolvers import reverse

from apps_productdata.mentoki_product.models.courseproductgroup \
    import CourseProductGroup
from apps_pagedata.public.models import StaticPublicPages
from apps_accountdata.userprofiles.models.mentor import MentorsProfile


def server_error(request):
    # one of the things ‘render’ does is add ‘STATIC_URL’ to
    # the context, making it available from within the template.
    response = render(request, '500.html')
    response.status_code = 500
    return response

def maintenance_mode(request):
    # one of the things ‘render’ does is add ‘STATIC_URL’ to
    # the context, making it available from within the template.
    response = render(request, '503.html')
    response.status_code = 503
    return response


class StaticViewSitemap(Sitemap):
    changefreq = "monthly"

    def items(self):
        return ['home:home', 'contact:contact']

    def location(self, item):
        return reverse(item)

    def priority(self, item):
        if item == 'home:home':
            return 0.8
        else:
            return 0.5


class PublicViewSitemap(Sitemap):
    changefreq = "monthly"

    def items(self):
        return StaticPublicPages.objects.all()

    def priority(self, item):
        return 0.5


class CoursesViewSitemap(Sitemap):
    changefreq = "monthly"

    def items(self):
        courseproductgroup = CourseProductGroup.objects.published()
        return courseproductgroup

    def priority(self, item):
        if item.can_be_booked_now:
            return 1.0
        else:
            return 0.5


class CourseListViewSitemap(Sitemap):
    changefreq = "monthly"

    def items(self):
        return ['storefront:list_now', 'storefront:list', 'storefront:list_preview']

    def location(self, item):
        return reverse(item)

    def priority(self, item):
        if item == 'storefront:list_now':
            return 0.8
        else:
            return 0.5


class MentorsViewSitemap(Sitemap):
    changefreq = "monthly"

    def items(self):
        mentors = MentorsProfile.objects.mentors_all()
        return mentors

    def priority(self, item):
        if item == 'home:home':
            return 0.5
        else:
            return 0.5