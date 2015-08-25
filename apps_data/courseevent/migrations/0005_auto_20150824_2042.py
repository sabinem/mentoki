# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_prices.models


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0004_auto_20150823_2223'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseevent',
            name='price',
            field=django_prices.models.PriceField(default=0, currency='ECU', verbose_name='Price', max_digits=12, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='courseevent',
            name='start_date',
            field=models.DateField(help_text='im Format Tag.Monat.Jahr angeben', null=True, verbose_name='Startdatum', blank=True),
        ),
        migrations.AlterField(
            model_name='courseevent',
            name='status_external',
            field=models.CharField(default='0', max_length=2, choices=[('0', 'nicht \xf6ffentlich'), ('1', 'zur Buchung ge\xf6ffnet'), ('1', 'Buchung abgeschlossen'), ('2', 'Vorschau')]),
        ),
        migrations.AlterField(
            model_name='courseevent',
            name='status_internal',
            field=models.CharField(default='0', max_length=2, choices=[('0', 'nicht ver\xf6ffentlicht'), ('1', 'offen zur Buchung'), ('a', 'Vorschau')]),
        ),
    ]
