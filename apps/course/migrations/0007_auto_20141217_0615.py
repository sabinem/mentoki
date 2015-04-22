# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_auto_20141215_0603'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursematerialunit',
            name='excerpt',
        ),
        migrations.RemoveField(
            model_name='courseunit',
            name='excerpt',
        ),
    ]
