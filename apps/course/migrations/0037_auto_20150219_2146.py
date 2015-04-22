# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0036_auto_20150219_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursematerialunit',
            name='slug',
            field=models.SlugField(unique=True),
            preserve_default=True,
        ),
    ]
