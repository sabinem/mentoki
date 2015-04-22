# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0023_courseevent_structure'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseeventpubicinformation',
            name='excerpt',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
