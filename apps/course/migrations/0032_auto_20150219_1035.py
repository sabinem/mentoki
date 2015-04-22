# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0031_auto_20150219_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursematerialunit',
            name='slug',
            field=models.SlugField(),
            preserve_default=True,
        ),
    ]
