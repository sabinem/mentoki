# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0006_auto_20150824_2045'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroommenuitem',
            name='is_publishlink',
            field=models.BooleanField(default=True, help_text='Links deren setzen Objekte im Klassenzimmer ver\xf6ffentlicht.\n        Das ist bei Lektionen und Foren der Fall', verbose_name='aktiv'),
        ),
        migrations.AddField(
            model_name='classroommenuitem',
            name='is_shortlink',
            field=models.BooleanField(default=True, help_text='die wichtigsten Links werden als Kurzlinks angezeigt.\n        Es sollte nicht mehr als 10 Kurzlinks geben', verbose_name='Kurzlink'),
        ),
        migrations.AlterField(
            model_name='classroommenuitem',
            name='active',
            field=models.BooleanField(),
        ),
    ]
