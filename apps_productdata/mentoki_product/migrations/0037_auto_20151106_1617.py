# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0036_courseproduct_newcurrency'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courseproduct',
            old_name='currency',
            new_name='oldcurrency',
        ),
    ]
