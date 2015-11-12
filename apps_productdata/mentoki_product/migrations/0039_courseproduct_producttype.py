# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0038_auto_20151106_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseproduct',
            name='producttype',
            field=models.IntegerField(default=20),
        ),
    ]
