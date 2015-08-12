# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0034_auto_20150811_0621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroommenuitem',
            name='item_type',
            field=models.CharField(help_text='Welcher Art ist der Men\xfceintrag: \xdcberschrift, Link, etc?', max_length=15, verbose_name='Typ des Men\xfcpunkts', choices=[('forum', 'Forum'), ('lesson', 'Unterricht'), ('announcements', 'Ank\xfcndigungen'), ('homework', 'Hausaufgabe'), ('last_posts', 'Neueste Beitr\xe4ge'), ('private', 'Privatbereich'), ('header', '\xdcberschrift'), ('participants', 'Teilnehmerliste')]),
        ),
        migrations.AlterField(
            model_name='courseevent',
            name='target_group',
            field=models.TextField(help_text='Zielgruppe, wie sie in der Kursausschreibung erscheinen soll.', verbose_name='Zielgruppe', blank=True),
        ),
    ]
