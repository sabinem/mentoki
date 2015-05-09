# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0027_auto_20150426_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseeventpubicinformation',
            name='video_url',
            field=models.CharField(max_length=30, verbose_name='K\xfcrzel des Videos bei You Tube: Bsp: wenn das der Url ist: https://www.youtube.com/watch?v=wF4WD-LGoU0,dann ist wF4WD-LGoU0 das K\xfcrzel!Kursbeschreibung, wenn ausgef\xfcllt', blank=True),
            preserve_default=True,
        ),
    ]
