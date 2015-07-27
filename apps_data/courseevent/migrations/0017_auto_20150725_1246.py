# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0016_auto_20150725_0752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroommenuitem',
            name='display_title',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='classroommenuitem',
            name='item_type',
            field=models.CharField(max_length=15, choices=[('forum', 'Forum'), ('lesson', 'Unterricht'), ('anouncements', 'Ank\xfcndigungen'), ('homework', 'homework'), ('last_posts', 'latest forum posts'), ('private', 'students private place'), ('header', 'header'), ('participants', 'participants list')]),
        ),
    ]
