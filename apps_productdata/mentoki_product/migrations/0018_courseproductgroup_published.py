# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0017_auto_20151018_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseproductgroup',
            name='published',
            field=models.BooleanField(default=True),
        ),
    ]
