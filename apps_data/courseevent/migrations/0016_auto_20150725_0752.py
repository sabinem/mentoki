# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0015_auto_20150724_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroommenuitem',
            name='item_type',
            field=models.CharField(max_length=15, choices=[('forum', 'Forum'), ('lesson', 'Unterricht'), ('anouncements', 'Ank\xfcndigungen'), ('homework', 'homework'), ('last_posts', 'latest forum posts'), ('private', 'students private place'), ('header', 'header')]),
        ),
    ]
