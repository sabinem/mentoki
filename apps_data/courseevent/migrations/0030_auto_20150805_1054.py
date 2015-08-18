# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0029_auto_20150802_0747'),
    ]

    operations = [
        migrations.AddField(
            model_name='forum',
            name='description',
            field=models.TextField(help_text='Die Kurzbeschreibung erscheint auf der \xdcbersichtsseite der Foren.', max_length=200, verbose_name='Kurzbeschreibung', blank=True),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='published',
            field=models.BooleanField(default=False, verbose_name='ver\xf6ffentlichen?'),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='published_at',
            field=model_utils.fields.MonitorField(default=django.utils.timezone.now, when=set([True]), verbose_name='ver\xf6ffentlicht am', monitor='published'),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='text',
            field=models.TextField(verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Betreff'),
        ),
        migrations.AlterField(
            model_name='forum',
            name='display_nr',
            field=models.IntegerField(help_text='steuert die Anzeigereihenfolge der UnterForen innerhalb des \xfcbergeordneten Forums', verbose_name='Anzeigenummer'),
        ),
        migrations.AlterField(
            model_name='forum',
            name='text',
            field=models.TextField(help_text='Dieser Text wird den Forumsbeitr\xe4gen vorangestellt und leitet die Kursteilnehmern an, ihre\n                  Beitr\xe4ge zu schreiben.', verbose_name='Beschreibung des Forums', blank=True),
        ),
        migrations.AlterField(
            model_name='forum',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Forums-Titel'),
        ),
        migrations.AlterField(
            model_name='homework',
            name='lesson',
            field=models.ForeignKey(verbose_name='Bezug auf einen Lernabschnitt?', blank=True, to='course.Lesson', null=True),
        ),
        migrations.AlterField(
            model_name='homework',
            name='published',
            field=models.BooleanField(default=False, verbose_name='ver\xf6ffentlichen'),
        ),
        migrations.AlterField(
            model_name='homework',
            name='title',
            field=models.CharField(max_length=100, verbose_name='\xdcberschrift'),
        ),
    ]
