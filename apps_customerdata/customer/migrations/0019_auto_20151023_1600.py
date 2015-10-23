# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_auto_20150929_1005'),
        ('customer', '0018_auto_20151022_2024'),
    ]

    operations = [
        migrations.CreateModel(
            name='FailedTransaction',
            fields=[
                ('amount', models.DecimalField(verbose_name='amount', max_digits=20, decimal_places=4)),
                ('currency', models.CharField(default=b'USD', max_length=3, verbose_name='currency')),
                ('braintree_transaction_id', models.CharField(default=b'x', max_length=50, serialize=False, primary_key=True)),
                ('braintree_merchant_account_id', models.CharField(default=b'default', max_length=100, verbose_name=b'braintree_merchant')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('braintree_result', models.TextField(blank=True)),
                ('course', models.ForeignKey(blank=True, to='course.Course', null=True)),
                ('customer', models.ForeignKey(to='customer.Customer')),
            ],
            options={
                'verbose_name': 'Nicht erfolgreiche Transaktion',
                'verbose_name_plural': 'Nicht erfolgreiche Transaktionen',
            },
        ),
        migrations.CreateModel(
            name='SuccessfulTransaction',
            fields=[
                ('amount', models.DecimalField(verbose_name='amount', max_digits=20, decimal_places=4)),
                ('currency', models.CharField(default=b'USD', max_length=3, verbose_name='currency')),
                ('braintree_transaction_id', models.CharField(default=b'x', max_length=50, serialize=False, primary_key=True)),
                ('braintree_merchant_account_id', models.CharField(default=b'default', max_length=100, verbose_name=b'braintree_merchant')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(blank=True, to='course.Course', null=True)),
                ('customer', models.ForeignKey(to='customer.Customer')),
            ],
            options={
                'verbose_name': 'Erfolgreiche Transaktion',
                'verbose_name_plural': 'Erfolgreiche Transaktionen',
            },
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='courseproduct',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='temporder',
            name='error_code_braintree_customer',
        ),
        migrations.RemoveField(
            model_name='temporder',
            name='error_code_braintree_transaction',
        ),
        migrations.RemoveField(
            model_name='temporder',
            name='success',
        ),
        migrations.AddField(
            model_name='order',
            name='course',
            field=models.ForeignKey(blank=True, to='course.Course', null=True),
        ),
        migrations.DeleteModel(
            name='Transaction',
        ),
        migrations.AddField(
            model_name='successfultransaction',
            name='order',
            field=models.ForeignKey(to='customer.Order'),
        ),
        migrations.AddField(
            model_name='failedtransaction',
            name='temporder',
            field=models.ForeignKey(to='customer.TempOrder'),
        ),
    ]
