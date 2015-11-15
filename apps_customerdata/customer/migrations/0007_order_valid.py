# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_order_nr_part_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='valid',
            field=models.BooleanField(default=False),
        ),
    ]
