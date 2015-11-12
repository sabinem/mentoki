# coding: utf-8

"""
Admin for Customers-Data, Transactions and Orders
"""

from __future__ import unicode_literals, absolute_import

from django.contrib import admin

from .models.customer import Customer
from .models.transaction import Transaction
from .models.order import Order

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
    list_display = ('id', 'amount', 'success', 'course',
                    'braintree_transaction_id')
    list_filter = ('course', 'created', 'success')

@admin.register(Order)
class Order(admin.ModelAdmin):
    """
    Orders are between registered user only since they are listed here only after
    payment occured and the the users got registered
    """
    list_display = ('id', 'courseproduct', 'customer', )
