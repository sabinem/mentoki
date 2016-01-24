# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0066_courseproductgroupfield_background_color_hex'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseproductgroupfield',
            name='background_color_hex',
        ),
        migrations.AddField(
            model_name='courseproductgroup',
            name='background_color_hex',
            field=models.CharField(default='ddd', max_length=7),
            preserve_default=False,
        ),
    ]
