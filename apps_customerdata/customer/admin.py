# coding: utf-8

"""
Admin for Customers-Data, Transactions and Orders
"""

from __future__ import unicode_literals, absolute_import

from django.contrib import admin

from .models.customer import Customer
from .models.transaction import Transaction
from .models.order import Order
from .models.contact import Prebooking
from .models.braintreelog import BraintreeLog

#TODO determine later on what exactly is needed in the admin

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    """
    Customers that pay and are registered at braintree, the payment provider
    """
    list_display = ( 'id', 'user', 'braintree_customer_id', 'created')
    list_filter = ('user', 'created')


@admin.register(Transaction)
class Transaction(admin.ModelAdmin):
    """
    Transactions that occur when payment happens, they are also registered at braintree,
    the payment provider
    """
    list_display = ('id', 'order', 'success', 'course',
                    'braintree_transaction_id')
    list_filter = ('course', 'created', 'success' ,'order')

@admin.register(Order)
class Order(admin.ModelAdmin):
    """
    Orders are between registered user only since they are listed here only after
    payment occured and the the users got registered
    """
    list_display = ('id', 'courseproduct', 'customer', 'course',
                    'order_status', 'last_transaction_had_success', 'amount_paid',
                    'amount_per_payment',
                    'total_parts', 'started_to_pay', 'fully_paid', 'pay_in_parts')
    list_filter = ('courseproduct__course', 'courseproduct', 'customer', 'course')

@admin.register(Prebooking)
class CustomerAdmin(admin.ModelAdmin):
    """
    Customers that pay and are registered at braintree, the payment provider
    """
    list_display = ( 'id', 'email', 'interested_in_learning', 'created')
    list_filter = ('email', 'created')


@admin.register(BraintreeLog)
class BraintreeLogAdmin(admin.ModelAdmin):
    """
    Customers that pay and are registered at braintree, the payment provider
    """
    list_display = ( 'id', 'mentoki_transaction', 'created')
    list_filter = ('created', )
