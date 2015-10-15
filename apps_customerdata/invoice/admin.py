# coding: utf-8

"""
Admin for Course and its relation to User: CourseOwner
"""

from __future__ import unicode_literals, absolute_import

from django.contrib import admin

from .models.invoice import Invoice


@admin.register(Invoice)
class Invoice(admin.ModelAdmin):
    """
    Courses are time independent collections of teaching material, that are
    set up and owned by teachers.
    """
    list_display = ('product', 'customer', 'amount', 'invoice_nr'
                     )
    readonly_fields = ('invoice_nr',)


