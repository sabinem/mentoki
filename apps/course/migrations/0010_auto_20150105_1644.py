# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0009_auto_20150105_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursematerialunit',
            name='url',
            field=models.URLField(default=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='courseunit',
            name='url',
            field=models.URLField(default=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coursematerialunit',
            name='text',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='courseunit',
            name='text',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
