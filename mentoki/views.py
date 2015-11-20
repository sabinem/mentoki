# -*- coding: utf-8 -*-

from django.contrib.sitemaps import Sitemap
from django.shortcuts import render

from apps_productdata.mentoki_product.models.courseproductgroup \
    import CourseProductGroup


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


class MentokiSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return CourseProductGroup.objects.all()

    def items(self):
        return ['main', 'about', 'license']

    def location(self, item):
        return reverse(item)