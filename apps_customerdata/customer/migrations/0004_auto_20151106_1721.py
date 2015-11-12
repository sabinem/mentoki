# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_auto_20151106_1717'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='order_status',
            new_name='order_statusx',
        ),
    ]
