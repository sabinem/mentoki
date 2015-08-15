# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0039_auto_20150813_1100'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseeventparticipation',
            name='hidden',
            field=models.BooleanField(default=False, verbose_name='versteckt'),
        ),
        migrations.AddField(
            model_name='forum',
            name='hidden',
            field=models.BooleanField(default=False, verbose_name='versteckt'),
        ),
    ]
