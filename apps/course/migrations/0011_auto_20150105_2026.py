# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0010_auto_20150105_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursematerialunit',
            name='url',
            field=models.URLField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='courseunit',
            name='url',
            field=models.URLField(blank=True),
            preserve_default=True,
        ),
    ]
