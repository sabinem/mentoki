# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0005_auto_20150917_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='classlesson',
            name='show_work_area',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='lesson',
            name='show_work_area',
            field=models.BooleanField(default=True),
        ),
    ]
