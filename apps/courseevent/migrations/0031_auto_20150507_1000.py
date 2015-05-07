# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0030_auto_20150426_2113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseevent',
            name='format',
        ),
        migrations.RemoveField(
            model_name='courseevent',
            name='project',
        ),
        migrations.RemoveField(
            model_name='courseevent',
            name='structure',
        ),
        migrations.RemoveField(
            model_name='courseevent',
            name='text',
        ),
        migrations.RemoveField(
            model_name='courseevent',
            name='workload',
        ),
    ]
