# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0015_auto_20151123_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='braintreelog',
            name='result',
            field=models.BooleanField(default=False),
        ),
    ]
