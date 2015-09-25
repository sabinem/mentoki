# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0002_auto_20150916_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='classlesson',
            name='is_master',
            field=models.BooleanField(default=True),
        ),
    ]
