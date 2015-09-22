# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0008_auto_20150917_1052'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseevent',
            name='pricemodel',
            field=models.TextField(help_text='Skizziere Dein Wunsch-Preis-Modell f\xfcr diesen Kurs.', verbose_name='Preis Modell', blank=True),
        ),
    ]
