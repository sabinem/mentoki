# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0013_auto_20151014_0730'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('amount', models.DecimalField(verbose_name='amount', max_digits=20, decimal_places=4)),
                ('currency', models.CharField(default=b'EUR', max_length=3, verbose_name='currency')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('invoice_nr', models.AutoField(serialize=False, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('paid', models.BooleanField()),
                ('customer', models.ForeignKey(to='customer.Customer')),
                ('product', models.ForeignKey(to='mentoki_product.CourseEventProduct')),
            ],
        ),
    ]
