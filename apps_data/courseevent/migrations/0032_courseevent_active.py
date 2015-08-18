# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0031_auto_20150805_1057'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseevent',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
