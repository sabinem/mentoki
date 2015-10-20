# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_order_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_paid',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='order',
            name='transaction',
            field=models.ManyToManyField(to='customer.Transaction'),
        ),
    ]
