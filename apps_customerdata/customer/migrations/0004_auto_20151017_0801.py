# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0014_auto_20151014_1324'),
        ('customer', '0003_auto_20151016_2324'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('amount', models.DecimalField(verbose_name='amount', max_digits=20, decimal_places=4)),
                ('currency', models.CharField(default=b'USD', max_length=3, verbose_name='currency')),
                ('braintree_transaction_id', models.CharField(default=b'x', max_length=50, serialize=False, primary_key=True)),
                ('braintree_merchant_account_id', models.CharField(default=b'default', max_length=100, verbose_name=b'braintree_merchant')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Transaktion',
                'verbose_name_plural': 'Transaktionen',
            },
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': 'Kunde', 'verbose_name_plural': 'Kunden'},
        ),
        migrations.AddField(
            model_name='transaction',
            name='customer',
            field=models.ForeignKey(to='customer.Customer'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='product',
            field=models.ForeignKey(to='mentoki_product.CourseEventProduct'),
        ),
    ]
