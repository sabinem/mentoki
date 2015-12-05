# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0055_auto_20151204_1958'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseproductgroupfield',
            name='display_left',
            field=models.BooleanField(default=True),
        ),
    ]
