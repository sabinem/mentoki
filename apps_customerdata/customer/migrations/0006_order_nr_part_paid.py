# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_auto_20151113_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='nr_part_paid',
            field=models.IntegerField(default=1),
        ),
    ]
