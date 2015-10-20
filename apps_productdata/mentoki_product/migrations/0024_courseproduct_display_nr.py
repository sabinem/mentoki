# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0023_courseproductgroup_discount_text_long'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseproduct',
            name='display_nr',
            field=models.IntegerField(default=1),
        ),
    ]
