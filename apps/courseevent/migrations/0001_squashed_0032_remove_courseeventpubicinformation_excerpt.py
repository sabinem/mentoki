# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import model_utils.fields


class Migration(migrations.Migration):

    replaces = [(b'courseevent', '0001_initial'), (b'courseevent', '0002_courseevent_format'), (b'courseevent', '0003_auto_20141212_1824'), (b'courseevent', '0004_auto_20141212_1824'), (b'courseevent', '0005_auto_20141215_0603'), (b'courseevent', '0006_auto_20141218_0605'), (b'courseevent', '0007_courseevent_project'), (b'courseevent', '0008_courseeventparticipation_url'), (b'courseevent', '0009_participantpages'), (b'courseevent', '0010_auto_20150105_2230'), (b'courseevent', '0011_remove_courseeventparticipation_url'), (b'courseevent', '0012_auto_20150105_2256'), (b'courseevent', '0013_auto_20150130_2058'), (b'courseevent', '0014_courseeventparticipation'), (b'courseevent', '0015_auto_20150219_1026'), (b'courseevent', '0016_auto_20150327_1115'), (b'courseevent', '0017_auto_20150403_1657'), (b'courseevent', '0018_auto_20150405_1710'), (b'courseevent', '0019_auto_20150413_1119'), (b'courseevent', '0020_remove_courseeventpubicinformation_excerpt'), (b'courseevent', '0021_remove_courseeventpubicinformation_user'), (b'courseevent', '0022_auto_20150413_1439'), (b'courseevent', '0023_courseevent_structure'), (b'courseevent', '0024_courseeventpubicinformation_excerpt'), (b'courseevent', '0025_auto_20150424_1029'), (b'courseevent', '0026_courseevent_video_url'), (b'courseevent', '0027_auto_20150426_2035'), (b'courseevent', '0028_auto_20150426_2111'), (b'courseevent', '0029_auto_20150426_2111'), (b'courseevent', '0030_auto_20150426_2113'), (b'courseevent', '0031_auto_20150507_1000'), (b'courseevent', '0032_remove_courseeventpubicinformation_excerpt')]

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '__first__'),
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
                ('text', models.TextField()),
                ('excerpt', models.TextField()),
                ('start_date', models.DateField(null=True, blank=True)),
                ('nr_weeks', models.IntegerField(null=True, blank=True)),
                ('max_participants', models.IntegerField(null=True, blank=True)),
                ('event_type', models.CharField(default=b'0', max_length=2, choices=[(b'0', b'begleiteter Gruppenkurs / mit Termin'), (b'1', b'internes Diskussionsforum / ohne Termin / nicht gelistet '), (b'2', b'unbegleitetes Selbstlernen / ohne Termin'), (b'3', b'begleitetes Selbstlernen / ohne Termin')])),
                ('status_external', models.CharField(default=b'0', max_length=2, choices=[(b'0', b'noch unveroeffentlicht'), (b'2', b'zur Buchung geoeffnet'), (b'3', b'Buchung abgeschlossen'), (b'4', b'nicht mehr gelistet')])),
                ('status_internal', models.CharField(default=b'0', max_length=2, choices=[(b'0', b'im Aufbau'), (b'1', b'Klassenzimmer geoeffnet'), (b'2', b'abgeschlossen / beendet')])),
                ('course', models.ForeignKey(to='course.Course')),
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
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='courseevent',
            name='format',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='courseevent',
            name='workload',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='courseevent',
            name='excerpt',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='courseevent',
            name='text',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='courseevent',
            name='project',
            field=models.TextField(default=b'x', blank=True),
            preserve_default=True,
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
        migrations.AlterField(
            model_name='courseevent',
            name='status_external',
            field=models.CharField(default=b'0', max_length=2, choices=[(b'0', b'noch unveroeffentlicht'), (b'2', b'zur Buchung geoeffnet'), (b'3', b'Buchung abgeschlossen'), (b'4', b'offen fuer interne Buchung')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='courseevent',
            name='event_type',
            field=models.CharField(default=b'0', max_length=2, choices=[(b'0', b'Gruppenkurs'), (b'1', b'internes Diskussionsforum / ohne Termin / nicht gelistet '), (b'2', b'unbegleitetes Selbstlernen / ohne Termin'), (b'3', b'begleitetes Selbstlernen / ohne Termin')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='courseevent',
            name='status_external',
            field=models.CharField(default=b'0', max_length=2, choices=[(b'0', b'noch unveroeffentlicht'), (b'1', b'Vorankuendigung'), (b'2', b'zur Buchung geoeffnet'), (b'3', b'Buchung abgeschlossen'), (b'4', b'Kursereignis abgeschlossen')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='courseevent',
            name='status_internal',
            field=models.CharField(default=b'1', max_length=2, choices=[(b'1', b'im Aufbau'), (b'0', b'zur internen Buchung geoeffnet'), (b'2', b'keine interne Buchung mehr moeglich')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='courseevent',
            name='status_external',
            field=models.CharField(default='0', max_length=2, choices=[('0', 'noch unver\xf6ffentlicht'), ('1', 'Vorank\xfcndigung'), ('2', 'zur Buchung ge\xf6ffnet'), ('3', 'Buchung abgeschlossen'), ('4', 'Kursereignis abgeschlossen')]),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='CourseEventPubicInformation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('text', models.TextField(verbose_name='freie Kursbeschreibung, \xfcberschreibt die allgemeine Kursbeschreibung, wenn ausgef\xfcllt', blank=True)),
                ('format', models.TextField(verbose_name='Kursformat', blank=True)),
                ('workload', models.TextField(verbose_name='Arbeitsbelastung', blank=True)),
                ('target_group', models.TextField(verbose_name='Zielgruppe, , \xfcberschreibt die allgemeine Kursbeschreibung, wenn ausgef\xfcllt', blank=True)),
                ('prerequisites', models.TextField(verbose_name='Voraussetzungen, , \xfcberschreibt die allgemeine Kursbeschreibung, wenn ausgef\xfcllt', blank=True)),
                ('project', models.TextField(verbose_name='Teilnehmernutzen, \xfcberschreibt die allgemeine Kursbeschreibung, wenn ausgef\xfcllt', blank=True)),
                ('structure', models.TextField(verbose_name='Gliederung', blank=True)),
                ('courseevent', models.ForeignKey(to='courseevent.CourseEvent')),
                ('video_url', models.CharField(max_length=100, verbose_name='K\xfcrzel des Videos bei You Tube ', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='courseevent',
            name='format',
        ),
        migrations.RemoveField(
            model_name='courseevent',
            name='workload',
        ),
        migrations.AlterField(
            model_name='courseevent',
            name='event_type',
            field=models.CharField(default='0', max_length=2, choices=[('0', 'gef\xfchrter Gruppenkurs'), ('1', 'internes Diskussionsforum / ohne Termin / nicht gelistet '), ('2', 'unbegleitetes Selbstlernen / ohne Termin'), ('3', 'begleitetes Selbstlernen / ohne Termin')]),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='courseevent',
            name='project',
        ),
        migrations.RemoveField(
            model_name='courseevent',
            name='text',
        ),
    ]
