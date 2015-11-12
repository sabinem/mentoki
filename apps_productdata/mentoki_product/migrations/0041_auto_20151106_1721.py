# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0040_auto_20151106_1721'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courseproduct',
            old_name='producttype',
            new_name='product_type',
        ),
    ]
