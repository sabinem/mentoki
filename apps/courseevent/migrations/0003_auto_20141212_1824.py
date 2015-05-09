# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0002_courseevent_format'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseevent',
            name='workload',
            field=models.TextField(default=b'text'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='courseevent',
            name='excerpt',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='courseevent',
            name='format',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='courseevent',
            name='text',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
