# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0035_courseproduct_product_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseproduct',
            name='newcurrency',
            field=models.IntegerField(default=1),
        ),
    ]
