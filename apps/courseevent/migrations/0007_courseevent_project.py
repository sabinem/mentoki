# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0006_auto_20141218_0605'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseevent',
            name='project',
            field=models.TextField(default=b'x', blank=True),
            preserve_default=True,
        ),
    ]
