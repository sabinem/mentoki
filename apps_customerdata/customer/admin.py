# coding: utf-8

"""
Admin for Customers-Data, Transactions and Orders
"""

from __future__ import unicode_literals, absolute_import

from django.contrib import admin

from .models.customer import Customer
from .models.transaction import SuccessfulTransaction, FailedTransaction
from .models.order import Order
from .models.temporder import TempOrder


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    """
    Customers that pay and are registered at braintree, the payment provider
    """
    list_display = ('braintree_customer_id', 'user', 'first_name', 'last_name', 'created' )
    list_filter = ('created','user')


@admin.register(SuccessfulTransaction)
class Transaction(admin.ModelAdmin):
    """
    Transactions that occur when payment happens, they are also registered at braintree,
    the payment provider
    """
    list_display = ('order', 'customer', 'amount', 'course')


@admin.register(FailedTransaction)
class Transaction(admin.ModelAdmin):
    """
    Transactions that occur when payment happens, they are also registered at braintree,
    the payment provider
    """
    list_display = ('temporder', 'customer', 'amount', 'course')


@admin.register(Order)
class Order(admin.ModelAdmin):
    """
    Orders are between registered user only since they are listed here only after
    payment occured and the the users got registered
    """
    list_display = ('courseproduct', 'customer', 'order_status', 'course')


@admin.register(TempOrder)
class TempOrder(admin.ModelAdmin):
    """
    Incomplete orders are listed here. It may make sense to send out an email,
    if someone attempted to book, but could not pay.
    """
    list_display = ('courseproduct', 'participant_email', 'user')