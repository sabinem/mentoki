# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0060_courseproductsubgroup_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseproductgroup',
            name='is_ready',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='courseproductgroupfield',
            name='is_ready',
            field=models.BooleanField(default=False),
        ),
    ]
