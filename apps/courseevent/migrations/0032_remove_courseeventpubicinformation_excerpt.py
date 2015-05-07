# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0031_auto_20150507_1000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseeventpubicinformation',
            name='excerpt',
        ),
    ]
