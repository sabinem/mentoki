# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseevent',
            name='format',
            field=models.TextField(default=b'text'),
            preserve_default=True,
        ),
    ]
