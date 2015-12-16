# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0061_auto_20151214_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseproductgroup',
            name='is_ready',
            field=models.BooleanField(default=False, verbose_name='fertig'),
        ),
        migrations.AlterField(
            model_name='courseproductgroupfield',
            name='is_ready',
            field=models.BooleanField(default=False, verbose_name='fertig'),
        ),
    ]
