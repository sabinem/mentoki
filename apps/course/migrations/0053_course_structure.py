# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0052_auto_20150413_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='structure',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
