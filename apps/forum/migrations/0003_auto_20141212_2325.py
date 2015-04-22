# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20141212_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='description',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subforum',
            name='description',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
