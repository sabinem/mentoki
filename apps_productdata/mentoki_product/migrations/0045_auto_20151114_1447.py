# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0044_remove_courseproduct_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseproduct',
            name='dependency',
        ),
        migrations.RemoveField(
            model_name='courseproduct',
            name='part_of',
        ),
    ]
