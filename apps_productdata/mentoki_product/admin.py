# coding: utf-8

"""
Admin for Course and its relation to User: CourseOwner
"""

from __future__ import unicode_literals, absolute_import

from django.contrib import admin

from .models.courseproduct import CourseProduct
from .models.courseproductgroup import CourseProductGroup, \
    CourseProductSubGroup, CourseProductGroupField
from .models.specialoffer import SpecialOffer


@admin.register(CourseProductGroup)
class CourseProductGroupAdmin(admin.ModelAdmin):
    """
    CourseProductGroup is the Group of all products related to a course
    """
    list_display = ('id', 'course', 'display_nr', 'slug')
    list_filter = ('course', 'modified')
    list_display_links = ('id',)


@admin.register(CourseProductSubGroup)
class CourseSubProductGroupAdmin(admin.ModelAdmin):
    """
    CourseProductGroup is the Group of all products related to a course
    """
    list_display = ('id', 'course', 'name')
    list_filter = ('course', 'modified')
    list_display_links = ('id',)


@admin.register(CourseProduct)
class CourseProductAdmin(admin.ModelAdmin):
    """
    Course products are products related to Courses
    """
    list_display = ('id', 'name', 'course', 'courseevent', 'courseproductsubgroup',
                    'price' , 'sales_price', 'get_currency_display',  'display_nr',
                    'get_product_type_display')
    list_filter = ('course', 'modified')
    list_display_links = ('id',)


@admin.register(SpecialOffer)
class SpecialOfferAdmin(admin.ModelAdmin):
    """
    Offers and their reach on products
    """
    list_display = ('id', 'offerreach', 'course', 'percentage_off')
    list_filter = ('course', 'modified')
    list_display_links = ('id',)


@admin.register(CourseProductGroupField)
class CourseProductGroupFieldAdmin(admin.ModelAdmin):
    """
    CourseProductGroup is the Group of all products related to a course
    """
    list_display = ('id', 'course', 'courseproductgroup', 'published',
                    'title', 'pagemark', 'display_nr')
    list_filter = ('course', 'modified')
    list_display_links = ('id',)
