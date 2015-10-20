# coding: utf-8

"""
Admin for Course and its relation to User: CourseOwner
"""

from __future__ import unicode_literals, absolute_import

from django.contrib import admin

from .models.customer import Customer
from .models.transaction import Transaction
from .models.order import Order


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    """
    Courses are time independent collections of teaching material, that are
    set up and owned by teachers.
    """
    list_display = ('braintree_customer_id', 'user', 'first_name', 'last_name', 'created' )
    list_filter = ('created','user')



@admin.register(Transaction)
class Transaction(admin.ModelAdmin):
    """
    Courses are time independent collections of teaching material, that are
    set up and owned by teachers.
    """
    list_display = ('courseproduct', 'customer', 'amount')



@admin.register(Order)
class Order(admin.ModelAdmin):
    """
    Courses are time independent collections of teaching material, that are
    set up and owned by teachers.
    """
    list_display = ('courseproduct', 'customer', 'order_status')
