# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0003_auto_20141212_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseevent',
            name='workload',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
