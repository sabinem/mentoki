# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0021_remove_courseeventpubicinformation_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseeventpubicinformation',
            name='project',
            field=models.TextField(verbose_name='Teilnehmernutzen, \xfcberschreibt die allgemeine Kursbeschreibung, wenn ausgef\xfcllt', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='courseeventpubicinformation',
            name='structure',
            field=models.TextField(verbose_name='Gliederung', blank=True),
            preserve_default=True,
        ),
    ]
