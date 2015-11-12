# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0039_courseproduct_producttype'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courseproduct',
            old_name='product_type',
            new_name='product_typex',
        ),
    ]
