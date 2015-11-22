# -*- coding: utf-8 -*-

from django.contrib.sitemaps import Sitemap
from django.shortcuts import render
from django.core.urlresolvers import reverse

from apps_productdata.mentoki_product.models.courseproductgroup \
    import CourseProductGroup
from apps_pagedata.public.models import StaticPublicPages


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
        if item.slug == 'mentoki-starterkurs':
            return 0.9
        elif item.slug == 'impressum':
            return 0.3
        else:
            return 0.5



class ProductViewSitemap(Sitemap):
    changefreq = "weekly"

    def items(self):
        groups = CourseProductGroup.objects.published()
        list =[]
        for group in groups:
            list.append({'productgroup_slug':group.slug,
                         'page': 'detail',
                         'productgroup':group})
            list.append({'productgroup_slug':group.slug,
                         'page': 'offer',
                         'productgroup':group})
            list.append({'productgroup_slug':group.slug,
                         'page': 'mentors',
                         'productgroup':group})
        #for group in groups:
        #    url = ('storefront:detail',
        #           kwargs={'slug': group.slug})
        #    list.append(url)
        return list

    def location(self, item):
        url = reverse('storefront:' + item['page'],
                      kwargs={'slug': item['productgroup_slug']})
        return url

    def priority(self, item):
        if item['productgroup'].can_be_booked_now:
            return 0.5
        else:
            return 0.8