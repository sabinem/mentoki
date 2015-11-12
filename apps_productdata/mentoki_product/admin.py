# coding: utf-8

"""
Admin for Course and its relation to User: CourseOwner
"""

from __future__ import unicode_literals, absolute_import

from django.contrib import admin

from .models.courseproduct import CourseProduct
from .models.courseproductgroup import CourseProductGroup
from .models.specialoffer import SpecialOffer


@admin.register(CourseProductGroup)
class CourseProductGroupAdmin(admin.ModelAdmin):
    """
    CourseProductGroup is the Group of all products related to a course
    """
    list_display = ('id', 'course', 'display_nr')
    list_filter = ('modified', 'course')
    list_display_links = ('id',)


@admin.register(CourseProduct)
class CourseProductAdmin(admin.ModelAdmin):
    """
    Course products are products related to Courses
    """
    list_display = ('id', 'name', 'course', 'product_type',
                    'dependency', 'part_of',
                    'price' , 'sales_price', 'display_nr')
    list_filter = ('modified', 'course')
    list_display_links = ('id',)


@admin.register(SpecialOffer)
class SpecialOfferAdmin(admin.ModelAdmin):
    """
    Offers and their reach on products
    """
    list_display = ('id', 'offerreach', 'course',)
    list_filter = ('modified', 'course')
    list_display_links = ('id',)

