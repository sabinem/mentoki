# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0007_auto_20150825_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='forum',
            name='has_published_decendants',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='classroommenuitem',
            name='is_publishlink',
            field=models.BooleanField(default=True, help_text='Links deren setzen Objekte im Klassenzimmer ver\xf6ffentlicht.\n        Das ist bei Lektionen und Foren der Fall', verbose_name='publishlink'),
        ),
        migrations.AlterField(
            model_name='homework',
            name='due_date',
            field=models.DateField(null=True, verbose_name='Abgabedatum', blank=True),
        ),
    ]
