# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0043_auto_20151113_1757'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseproduct',
            name='slug',
        ),
    ]
