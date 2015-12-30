# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0064_auto_20151219_1327'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseproductgroupfield',
            name='published',
            field=models.BooleanField(default=True),
        ),
    ]
