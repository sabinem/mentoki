# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0029_auto_20150426_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseeventpubicinformation',
            name='video_url',
            field=models.CharField(max_length=100, verbose_name='K\xfcrzel des Videos bei You Tube ', blank=True),
            preserve_default=True,
        ),
    ]
