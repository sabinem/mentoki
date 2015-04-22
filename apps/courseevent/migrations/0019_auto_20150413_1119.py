# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courseevent', '0018_auto_20150405_1710'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseEventPubicInformation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('text', models.TextField(verbose_name='freie Kursbeschreibung, \xfcberschreibt die allgemeine Kursbeschreibung, wenn ausgef\xfcllt', blank=True)),
                ('format', models.TextField(verbose_name='Kursformat', blank=True)),
                ('workload', models.TextField(verbose_name='Arbeitsbelastung', blank=True)),
                ('excerpt', models.TextField(verbose_name='Abstrakt, , \xfcberschreibt die allgemeine Kursbeschreibung, wenn ausgef\xfcllt', blank=True)),
                ('target_group', models.TextField(verbose_name='Zielgruppe, , \xfcberschreibt die allgemeine Kursbeschreibung, wenn ausgef\xfcllt', blank=True)),
                ('prerequisites', models.TextField(verbose_name='Voraussetzungen, , \xfcberschreibt die allgemeine Kursbeschreibung, wenn ausgef\xfcllt', blank=True)),
                ('project', models.TextField(default='x', verbose_name='Teilnehmerprojekt, , \xfcberschreibt die allgemeine Kursbeschreibung, wenn ausgef\xfcllt', blank=True)),
                ('structure', models.TextField(verbose_name='Gliederung, , \xfcberschreibt die allgemeine Kursbeschreibung, wenn ausgef\xfcllt', blank=True)),
                ('courseevent', models.ForeignKey(to='courseevent.CourseEvent')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='courseevent',
            name='format',
            field=models.TextField(verbose_name='Kursformat', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='courseevent',
            name='workload',
            field=models.TextField(verbose_name='Arbeitsbelastung', blank=True),
            preserve_default=True,
        ),
    ]
