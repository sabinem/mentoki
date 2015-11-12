# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0044_auto_20151106_1826'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialoffer',
            name='offerreach',
            field=models.IntegerField(default=1),
        ),
    ]
