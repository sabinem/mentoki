# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0013_auto_20150112_1157'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='status',
            field=models.CharField(default=b'0', max_length=2, choices=[(b'0', b'Im Aufbau'), (b'1', b'Fertig')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='takeaway',
            field=models.TextField(default=b'x', blank=True),
            preserve_default=True,
        ),
    ]
