# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0005_auto_20150828_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseevent',
            name='event_type',
            field=models.CharField(default='selflearn', max_length=12, verbose_name='Kursart', choices=[('guided', 'gef\xfchrter Gruppenkurs'), ('selflearn', 'Selbstlernen'), ('coached', 'Selbstlernen mit Unterst\xfctzung')]),
        ),
        migrations.AlterField(
            model_name='courseevent',
            name='status_external',
            field=models.CharField(default='0', max_length=2, verbose_name='externer Status', choices=[('0', 'nicht \xf6ffentlich'), ('1', 'zur Buchung ge\xf6ffnet'), ('1', 'Buchung abgeschlossen'), ('2', 'Vorschau')]),
        ),
        migrations.AlterField(
            model_name='courseevent',
            name='status_internal',
            field=models.CharField(default='0', max_length=2, verbose_name='interner Status', choices=[('0', 'nicht ver\xf6ffentlicht'), ('1', 'offen zur Buchung'), ('a', 'Vorschau')]),
        ),
    ]
