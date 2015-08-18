# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0033_auto_20150807_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroommenuitem',
            name='display_nr',
            field=models.IntegerField(help_text='An welcher Position im Men\xfc soll der Men\xfcpunkt angezeigt werden?', verbose_name='Reihenfolge Nummer'),
        ),
        migrations.AlterField(
            model_name='classroommenuitem',
            name='is_start_item',
            field=models.BooleanField(help_text='Welcher Men\xfcpunkt soll im Klassenzimmer als\n            erstes angesprungen werden?', verbose_name='Ist Startpunkt'),
        ),
        migrations.AlterField(
            model_name='classroommenuitem',
            name='item_type',
            field=models.CharField(help_text='Welcher Art ist der Men\xfceintrag: \xdcberschrift, Link, etc?', max_length=15, verbose_name='Typ des Men\xfcpunkts', choices=[('forum', 'Forum'), ('lesson', 'Unterricht'), ('anouncements', 'Ank\xfcndigungen'), ('homework', 'Hausaufgabe'), ('last_posts', 'Neueste Beitr\xe4ge'), ('private', 'Privatbereich'), ('header', '\xdcberschrift'), ('participants', 'Teilnehmerliste')]),
        ),
        migrations.AlterField(
            model_name='classroommenuitem',
            name='published',
            field=models.BooleanField(default=False, help_text='ist im Klassenzimmer-Men\xfc sichtbar', verbose_name='ver\xf6ffentlicht'),
        ),
        migrations.AlterField(
            model_name='courseevent',
            name='max_participants',
            field=models.IntegerField(null=True, verbose_name='Teilnehmeranzahl', blank=True),
        ),
    ]
