# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0009_auto_20151115_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='last_transaction_had_success',
            field=models.BooleanField(default=False),
        ),
    ]
