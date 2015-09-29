# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0015_auto_20150927_0901'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='announcement',
            options={'verbose_name': 'Ank\xfcndigung', 'verbose_name_plural': 'Ank\xfcndigungen'},
        ),
        migrations.AlterModelOptions(
            name='classroommenuitem',
            options={'verbose_name': 'Men\xfceintrag', 'verbose_name_plural': 'Men\xfceintr\xe4ge'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'Kommentar', 'verbose_name_plural': 'Kommentare'},
        ),
        migrations.AlterModelOptions(
            name='courseevent',
            options={'verbose_name': 'Kursereignis', 'verbose_name_plural': 'Kursereignisse'},
        ),
        migrations.AlterModelOptions(
            name='courseeventparticipation',
            options={'verbose_name': 'Kurs-Teilnehmer', 'verbose_name_plural': 'Kurs-Teilnehmer'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-modified'], 'verbose_name': 'Post (Forum)', 'verbose_name_plural': 'Posts (Forum)'},
        ),
        migrations.AlterModelOptions(
            name='studentswork',
            options={'verbose_name': 'Teilnehmer-Arbeit', 'verbose_name_plural': 'Teilnehmer-Arbeiten'},
        ),
        migrations.AlterModelOptions(
            name='thread',
            options={'ordering': ['-modified'], 'verbose_name': 'Beitrag (Forum)', 'verbose_name_plural': 'Beitr\xe4ge (Forum)'},
        ),
        migrations.AlterField(
            model_name='courseevent',
            name='price',
            field=models.DecimalField(null=True, verbose_name='Preis', max_digits=12, decimal_places=2, blank=True),
        ),
    ]
