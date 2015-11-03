# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0036_courseproduct_parallel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseproduct',
            name='parallel',
        ),
    ]
