# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0037_auto_20151106_1617'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courseproduct',
            old_name='newcurrency',
            new_name='currency',
        ),
    ]
