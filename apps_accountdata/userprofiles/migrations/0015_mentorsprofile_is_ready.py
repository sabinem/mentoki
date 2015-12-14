# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0014_auto_20151128_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentorsprofile',
            name='is_ready',
            field=models.BooleanField(default=False),
        ),
    ]
