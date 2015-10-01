# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20150929_1005'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_female',
            field=models.BooleanField(default=True),
        ),
    ]
