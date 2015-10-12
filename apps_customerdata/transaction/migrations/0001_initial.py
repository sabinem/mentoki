# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0012_auto_20151009_1412'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('amount', models.DecimalField(verbose_name='amount', max_digits=20, decimal_places=4)),
                ('currency', models.CharField(default=b'USD', max_length=3, verbose_name='currency')),
                ('braintree_transaction_id', models.CharField(default=b'x', max_length=50, serialize=False, primary_key=True)),
                ('braintree_customer_id', models.CharField(default=b'x', unique=True, max_length=36, verbose_name=b'braintree_customer_id')),
                ('braintree_merchant_account_id', models.CharField(default=b'default', max_length=100, verbose_name=b'braintree_merchant')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(to='customer.Customer')),
                ('product', models.ForeignKey(to='mentoki_product.CourseEventProduct')),
            ],
        ),
    ]
