# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseeventpubicinformation',
            name='prerequisites',
            field=models.TextField(verbose_name='Voraussetzungen', blank=True),
        ),
        migrations.AlterField(
            model_name='courseeventpubicinformation',
            name='project',
            field=models.TextField(verbose_name='Teilnehmernutzen', blank=True),
        ),
        migrations.AlterField(
            model_name='courseeventpubicinformation',
            name='target_group',
            field=models.TextField(verbose_name='Zielgruppe', blank=True),
        ),
        migrations.AlterField(
            model_name='courseeventpubicinformation',
            name='text',
            field=models.TextField(verbose_name='freie Kursbeschreibung', blank=True),
        ),
    ]
