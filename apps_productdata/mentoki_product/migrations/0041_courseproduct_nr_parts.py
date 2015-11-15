# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0040_auto_20151113_1319'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseproduct',
            name='nr_parts',
            field=models.IntegerField(default=1),
        ),
    ]
