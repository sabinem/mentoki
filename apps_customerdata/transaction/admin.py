# coding: utf-8

"""
Admin for Course and its relation to User: CourseOwner
"""

from __future__ import unicode_literals, absolute_import

from django.contrib import admin

from .models.transaction import Transaction


@admin.register(Transaction)
class Transaction(admin.ModelAdmin):
    """
    Courses are time independent collections of teaching material, that are
    set up and owned by teachers.
    """
    list_display = ('product', 'customer', 'amount',
                     )
    readonly_fields = ('braintree_transaction_id',)


