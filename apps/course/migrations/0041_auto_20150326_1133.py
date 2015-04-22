# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0040_auto_20150323_2145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='status',
        ),
        migrations.AddField(
            model_name='courseblock',
            name='status',
            field=models.CharField(default=b'0', max_length=2, choices=[(b'0', b'Im Aufbau'), (b'1', b'Fertig')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='coursematerialunit',
            name='status',
            field=models.CharField(default=b'0', max_length=2, choices=[(b'0', b'Im Aufbau'), (b'1', b'Fertig')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='courseunit',
            name='status',
            field=models.CharField(default=b'0', max_length=2, choices=[(b'0', b'Im Aufbau'), (b'1', b'Fertig')]),
            preserve_default=True,
        ),
    ]
