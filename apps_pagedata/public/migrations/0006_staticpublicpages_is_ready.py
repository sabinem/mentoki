# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0005_auto_20151123_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='staticpublicpages',
            name='is_ready',
            field=models.BooleanField(default=False),
        ),
    ]
