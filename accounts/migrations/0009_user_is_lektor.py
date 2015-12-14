# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20151124_1328'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_lektor',
            field=models.BooleanField(default=False),
        ),
    ]
