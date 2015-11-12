# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_auto_20151106_1722'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='oldcurrency',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_statusx',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='oldcurrency',
        ),
    ]
