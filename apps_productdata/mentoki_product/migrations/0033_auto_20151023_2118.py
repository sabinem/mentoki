# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0032_auto_20151023_1710'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courseproduct',
            old_name='has_depedencies',
            new_name='has_dependencies',
        ),
    ]
