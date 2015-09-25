# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0011_auto_20150917_1206'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentswork',
            name='publish_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='studentswork',
            name='republished',
            field=models.BooleanField(default=False, verbose_name='ver\xf6ffentlichen'),
        ),
        migrations.AddField(
            model_name='studentswork',
            name='republished_at',
            field=model_utils.fields.MonitorField(default=django.utils.timezone.now, when=set([True]), monitor='republished'),
        ),
        migrations.AlterField(
            model_name='classroommenuitem',
            name='is_start_item',
            field=models.BooleanField(default=False, help_text='Welcher Men\xfcpunkt soll im Klassenzimmer als\n            erstes angesprungen werden?', verbose_name='Ist Startpunkt'),
        ),
        migrations.AlterField(
            model_name='classroommenuitem',
            name='item_type',
            field=models.CharField(help_text='Welcher Art ist der Men\xfceintrag: \xdcberschrift, Link, etc?', max_length=15, verbose_name='Typ des Men\xfcpunkts', choices=[('header', '\xdcberschrift'), ('lesson', 'Lektion'), ('lessonstep', 'Lernschritt'), ('forum', 'Forum'), ('last_posts', 'Forum: neueste Beitr\xe4ge'), ('announcements', 'Ank\xfcndigungsliste'), ('private', 'Privatbereich der Kursteilnehmer'), ('participants', 'Teilnehmerliste')]),
        ),
    ]
