# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0029_auto_20151019_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseproductgroup',
            name='display_nr',
            field=models.IntegerField(default=1),
        ),
    ]
