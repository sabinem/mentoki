# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0002_auto_20150827_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='classlesson',
            name='is_original_lesson',
            field=models.BooleanField(default=True),
        ),
    ]
