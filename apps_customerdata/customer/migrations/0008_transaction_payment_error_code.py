# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_auto_20151106_1826'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='payment_error_code',
            field=models.IntegerField(default=0),
        ),
    ]
