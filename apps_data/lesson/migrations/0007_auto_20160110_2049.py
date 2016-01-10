# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0006_auto_20160110_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classlesson',
            name='show_work_area',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='show_work_area',
            field=models.BooleanField(default=False),
        ),
    ]
