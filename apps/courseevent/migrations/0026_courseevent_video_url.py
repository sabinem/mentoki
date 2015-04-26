# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0025_auto_20150424_1029'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseevent',
            name='video_url',
            field=models.URLField(blank=True),
            preserve_default=True,
        ),
    ]
