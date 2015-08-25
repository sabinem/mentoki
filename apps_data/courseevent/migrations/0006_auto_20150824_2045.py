# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_prices.models


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0005_auto_20150824_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseevent',
            name='price',
            field=django_prices.models.PriceField(decimal_places=2, currency='ECU', max_digits=12, blank=True, null=True, verbose_name='Price'),
        ),
    ]
