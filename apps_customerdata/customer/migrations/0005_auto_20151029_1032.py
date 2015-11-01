# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_auto_20151029_1011'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='flag_sucess',
            new_name='flag_payment_sucess',
        ),
        migrations.AddField(
            model_name='transaction',
            name='braintree_amount',
            field=models.CharField(max_length=10, verbose_name='amount form braintree', blank=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='braintree_payment_token',
            field=models.CharField(max_length=10, verbose_name=b'braintree Kundennr.', blank=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='braintree_customer_id',
            field=models.CharField(max_length=10, verbose_name=b'braintree Kundennr.', blank=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='braintree_merchant_account_id',
            field=models.CharField(max_length=20, verbose_name=b'braintree_merchant', blank=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='braintree_transaction_id',
            field=models.CharField(max_length=10, blank=True),
        ),
    ]
