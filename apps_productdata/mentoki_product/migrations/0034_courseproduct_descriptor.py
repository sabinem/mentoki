# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0033_auto_20151023_2118'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseproduct',
            name='descriptor',
            field=models.CharField(default='x', max_length=250),
        ),
    ]
