# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0019_auto_20150413_1119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseeventpubicinformation',
            name='excerpt',
        ),
    ]
