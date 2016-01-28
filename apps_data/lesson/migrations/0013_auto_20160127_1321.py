# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0012_questions'),
    ]

    operations = [
        migrations.AddField(
            model_name='classlesson',
            name='allow_questions',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='lesson',
            name='allow_questions',
            field=models.BooleanField(default=False),
        ),
    ]
