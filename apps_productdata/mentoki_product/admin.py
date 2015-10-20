# coding: utf-8

"""
Admin for Course and its relation to User: CourseOwner
"""

from __future__ import unicode_literals, absolute_import

from django.contrib import admin

from .models.courseevent import CourseEventProduct
from .models.courseproduct import CourseProduct
from .models.courseproductgroup import CourseProductGroup
from .models.specialoffer import SpecialOffer


@admin.register(CourseEventProduct)
class CourseEventProductAdmin(admin.ModelAdmin):
    """
    Courses are time independent collections of teaching material, that are
    set up and owned by teachers.
    """
    list_display = ('id', 'courseevent', 'modified', 'created')
    list_filter = ('modified', 'courseevent')
    list_display_links = ('id',)


@admin.register(CourseProduct)
class CourseProductAdmin(admin.ModelAdmin):
    """
    Courses are time independent collections of teaching material, that are
    set up and owned by teachers.
    """
    list_display = ('id', 'course', 'product_type', 'price' , 'sales_price', 'modified', 'created')
    list_filter = ('modified', 'course')
    list_display_links = ('id',)


@admin.register(CourseProductGroup)
class CourseProductGroupAdmin(admin.ModelAdmin):
    """
    Courses are time independent collections of teaching material, that are
    set up and owned by teachers.
    """
    list_display = ('id', 'course', 'modified', 'created')
    list_filter = ('modified', 'course')
    list_display_links = ('id',)



@admin.register(SpecialOffer)
class SpecialOfferAdmin(admin.ModelAdmin):
    """
    Courses are time independent collections of teaching material, that are
    set up and owned by teachers.
    """
    list_display = ('id', 'courseproduct', 'modified', 'created')
    list_filter = ('modified', 'course')
    list_display_links = ('id',)