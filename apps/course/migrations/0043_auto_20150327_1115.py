# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0042_auto_20150326_1150'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseblock',
            name='description',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='coursematerialunit',
            name='description',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='courseunit',
            name='description',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
    ]
