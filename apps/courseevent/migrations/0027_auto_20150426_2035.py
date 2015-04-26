# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0026_courseevent_video_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseevent',
            name='video_url',
        ),
        migrations.AddField(
            model_name='courseeventpubicinformation',
            name='video_url',
            field=models.URLField(blank=True),
            preserve_default=True,
        ),
    ]
