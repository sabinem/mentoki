# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0065_courseproductgroupfield_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseproductgroupfield',
            name='background_color_hex',
            field=models.CharField(default='ddd', max_length=7),
            preserve_default=False,
        ),
    ]
