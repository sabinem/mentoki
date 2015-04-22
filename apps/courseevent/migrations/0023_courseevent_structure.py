# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0022_auto_20150413_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseevent',
            name='structure',
            field=models.TextField(verbose_name='Gliederung', blank=True),
            preserve_default=True,
        ),
    ]
