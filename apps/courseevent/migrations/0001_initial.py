# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('slug', models.SlugField(unique=True)),
                ('title', models.CharField(max_length=100)),
                ('excerpt', models.TextField(blank=True)),
                ('start_date', models.DateField(null=True, blank=True)),
                ('nr_weeks', models.IntegerField(null=True, blank=True)),
                ('max_participants', models.IntegerField(null=True, blank=True)),
                ('event_type', models.CharField(default='0', max_length=2, choices=[('0', 'gef\xfchrter Gruppenkurs'), ('1', 'internes Diskussionsforum / ohne Termin / nicht gelistet '), ('2', 'unbegleitetes Selbstlernen / ohne Termin'), ('3', 'begleitetes Selbstlernen / ohne Termin')])),
                ('status_external', models.CharField(default='0', max_length=2, choices=[('0', 'noch unver\xf6ffentlicht'), ('1', 'Vorank\xfcndigung'), ('2', 'zur Buchung ge\xf6ffnet'), ('3', 'Buchung abgeschlossen'), ('4', 'Kursereignis abgeschlossen')])),
                ('status_internal', models.CharField(default='1', max_length=2, choices=[('1', 'im Aufbau'), ('0', 'zur internen Buchung geoeffnet'), ('2', 'keine interne Buchung mehr moeglich')])),
                ('course', models.ForeignKey(to='course.Course')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CourseEventParticipation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('courseevent', models.ForeignKey(to='courseevent.CourseEvent')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CourseEventPubicInformation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('video_url', models.CharField(max_length=100, verbose_name='K\xfcrzel des Videos bei You Tube ', blank=True)),
                ('text', models.TextField(verbose_name='freie Kursbeschreibung, \xfcberschreibt die allgemeine Kursbeschreibung, wenn ausgef\xfcllt', blank=True)),
                ('format', models.TextField(verbose_name='Kursformat', blank=True)),
                ('workload', models.TextField(verbose_name='Arbeitsbelastung', blank=True)),
                ('project', models.TextField(verbose_name='Teilnehmernutzen, \xfcberschreibt die allgemeine Kursbeschreibung, wenn ausgef\xfcllt', blank=True)),
                ('structure', models.TextField(verbose_name='Gliederung', blank=True)),
                ('target_group', models.TextField(verbose_name='Zielgruppe, , \xfcberschreibt die allgemeine Kursbeschreibung, wenn ausgef\xfcllt', blank=True)),
                ('prerequisites', models.TextField(verbose_name='Voraussetzungen, , \xfcberschreibt die allgemeine Kursbeschreibung, wenn ausgef\xfcllt', blank=True)),
                ('courseevent', models.ForeignKey(to='courseevent.CourseEvent')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CourseeventUnitPublish',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('published_at_date', models.DateTimeField(auto_now_add=True)),
                ('courseevent', models.ForeignKey(to='courseevent.CourseEvent')),
                ('unit', models.ForeignKey(to='course.CourseUnit')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
