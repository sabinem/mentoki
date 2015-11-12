# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0036_auto_20151112_2200'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseproduct',
            name='currency',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='courseproduct',
            name='product_type',
            field=models.IntegerField(default=20),
        ),
    ]
