# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0002_auto_20150607_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseevent',
            name='excerpt',
            field=models.TextField(verbose_name='Abstrakt', blank=True),
        ),
        migrations.AlterField(
            model_name='courseevent',
            name='max_participants',
            field=models.IntegerField(null=True, verbose_name='Teilnehmeranzahl', blank=True),
        ),
        migrations.AlterField(
            model_name='courseevent',
            name='nr_weeks',
            field=models.IntegerField(null=True, verbose_name='Wochenanzahl', blank=True),
        ),
        migrations.AlterField(
            model_name='courseevent',
            name='start_date',
            field=models.DateField(null=True, verbose_name='Startdatum', blank=True),
        ),
        migrations.AlterField(
            model_name='courseevent',
            name='status_external',
            field=models.CharField(default='0', max_length=2, verbose_name='Status extern', choices=[('0', 'noch unver\xf6ffentlicht'), ('1', 'Vorank\xfcndigung'), ('2', 'zur Buchung ge\xf6ffnet'), ('3', 'Buchung abgeschlossen'), ('4', 'Kursereignis abgeschlossen')]),
        ),
        migrations.AlterField(
            model_name='courseevent',
            name='status_internal',
            field=models.CharField(default='1', max_length=2, verbose_name='Status intern', choices=[('1', 'im Aufbau'), ('0', 'zur internen Buchung geoeffnet'), ('2', 'keine interne Buchung mehr moeglich')]),
        ),
    ]
