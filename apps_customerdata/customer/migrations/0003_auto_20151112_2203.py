# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20151112_2158'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_status',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='transaction',
            name='currency',
            field=models.IntegerField(default=1, verbose_name='W\xe4hrung'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='error_code',
            field=models.IntegerField(default=0),
        ),
    ]
