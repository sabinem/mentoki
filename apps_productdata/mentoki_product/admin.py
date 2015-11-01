# coding: utf-8

"""
Admin for Course and its relation to User: CourseOwner
"""

from __future__ import unicode_literals, absolute_import

from django.contrib import admin

from .models.courseproduct import CourseProduct
from .models.courseproductgroup import CourseProductGroup
from .models.specialoffer import SpecialOffer
from .models.producttype import ProductType


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
    list_display = ('id', 'reach', 'course', 'courseevent', 'courseproduct')
    list_filter = ('modified', 'course')
    list_display_links = ('id',)


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    """
    Product Types
    """
    list_display = ('id', 'name', 'is_part',
        'is_test', 'belongs_to_course', 'is_courseevent_participation', 'can_be_bought_only_once',
        'has_dependencies')
    list_display_links = ('id', 'name')