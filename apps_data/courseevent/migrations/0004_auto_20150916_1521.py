# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0003_classroommenuitem_icon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classroommenuitem',
            name='active',
        ),
        migrations.RemoveField(
            model_name='classroommenuitem',
            name='homework',
        ),
        migrations.RemoveField(
            model_name='classroommenuitem',
            name='is_forumlink',
        ),
        migrations.RemoveField(
            model_name='classroommenuitem',
            name='is_homeworklink',
        ),
        migrations.RemoveField(
            model_name='classroommenuitem',
            name='is_lessonlink',
        ),
        migrations.RemoveField(
            model_name='classroommenuitem',
            name='is_listlink',
        ),
        migrations.RemoveField(
            model_name='classroommenuitem',
            name='is_publishlink',
        ),
        migrations.RemoveField(
            model_name='classroommenuitem',
            name='optional',
        ),
        migrations.AlterField(
            model_name='classroommenuitem',
            name='item_type',
            field=models.CharField(help_text='Welcher Art ist der Men\xfceintrag: \xdcberschrift, Link, etc?', max_length=15, verbose_name='Typ des Men\xfcpunkts', choices=[('forum', 'Forum: Forum wird publiziert'), ('lesson', 'Unterricht: Lektion wird publiziert '), ('announcements', 'Link zu Ank\xfcndigungsliste'), ('last_posts', 'Link zu den neuesten Beitr\xe4ge'), ('private', 'Link zum Privatbereich der Kursteilnehmer'), ('header', '\xdcberschrift'), ('participants', 'Link zur Teilnehmerliste')]),
        ),
    ]
