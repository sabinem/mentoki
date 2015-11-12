# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0042_auto_20151106_1755'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProductType',
        ),
    ]
