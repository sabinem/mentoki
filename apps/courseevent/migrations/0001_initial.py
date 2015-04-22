# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import model_utils.fields


class Migration(migrations.Migration):

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
            name='CourseeventUnitPublish',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('publish_at_date', models.DateTimeField()),
                ('courseevent', models.ForeignKey(to='courseevent.CourseEvent')),
                ('unit', models.ForeignKey(to='course.CourseUnit')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
