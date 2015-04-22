# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0011_auto_20150105_2026'),
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
        migrations.AddField(
            model_name='coursematerialunit',
            name='urltype',
            field=models.CharField(default=b'1', max_length=2, choices=[(b'g', b'Google Doc'), (b'1', b'Keine externe Datei')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='courseunit',
            name='urltype',
            field=models.CharField(default=b'1', max_length=2, choices=[(b'g', b'Google Doc'), (b'1', b'Keine externe Datei')]),
            preserve_default=True,
        ),
    ]
