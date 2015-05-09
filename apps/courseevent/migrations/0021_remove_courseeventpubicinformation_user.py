# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0020_remove_courseeventpubicinformation_excerpt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseeventpubicinformation',
            name='user',
        ),
    ]
