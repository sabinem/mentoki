# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_auto_20151106_1721'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='orderstatus',
            new_name='order_status',
        ),
    ]
