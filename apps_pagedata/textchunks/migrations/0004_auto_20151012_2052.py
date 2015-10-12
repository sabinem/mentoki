# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textchunks', '0003_auto_20151012_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publictextchunks',
            name='pagecode',
            field=models.CharField(max_length=20, serialize=False, verbose_name='Code', primary_key=True),
        ),
    ]
