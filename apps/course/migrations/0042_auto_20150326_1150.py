# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0041_auto_20150326_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='status',
            field=models.CharField(default=b'0', max_length=2, choices=[(b'0', b'Im Aufbau'), (b'1', b'Fertig')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='courseowner',
            name='status',
            field=models.CharField(default=b'0', max_length=2, choices=[(b'0', b'Im Aufbau'), (b'1', b'Fertig')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(max_length=100, verbose_name=b'Ueberschrift'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='courseowner',
            name='text',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
