# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0007_auto_20160110_2049'),
    ]

    operations = [
        migrations.AddField(
            model_name='classlesson',
            name='is_numbered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='lesson',
            name='is_numbered',
            field=models.BooleanField(default=False),
        ),
    ]
