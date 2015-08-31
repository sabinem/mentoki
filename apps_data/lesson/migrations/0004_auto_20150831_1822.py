# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0003_classlesson_is_original_lesson'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classlesson',
            name='created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='classlesson',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
