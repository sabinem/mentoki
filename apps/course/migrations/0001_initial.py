# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
import django.utils.timezone
from django.conf import settings
import model_utils.fields
import apps.course.models
from apps.course.models import foto_location


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('text', models.TextField(verbose_name='Text', blank=True)),
                ('status', models.CharField(default='0', max_length=2, choices=[('0', 'Im Aufbau'), ('1', 'Fertig')])),
                ('title', models.CharField(max_length=100, verbose_name='\xdcberschrift')),
                ('slug', models.SlugField(unique=True)),
                ('excerpt', models.TextField(blank=True)),
                ('target_group', models.TextField(blank=True)),
                ('prerequisites', models.TextField(blank=True)),
                ('project', models.TextField(default='x', blank=True)),
                ('structure', models.TextField(blank=True)),
                ('email', models.EmailField(default='info@netteachers.de', max_length=75)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CourseBlock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('text', models.TextField(verbose_name='Text', blank=True)),
                ('status', models.CharField(default='0', max_length=2, choices=[('0', 'Im Aufbau'), ('1', 'Fertig')])),
                ('title', models.CharField(max_length=100, verbose_name='Ueberschrift')),
                ('display_nr', models.IntegerField(verbose_name='interne Nummer, steuert die Anzeigereihenfolge')),
                ('description', models.CharField(max_length=200, verbose_name='kurze Beschreibung', blank=True)),
                ('is_numbered', models.BooleanField(default=True)),
                ('show_full', models.BooleanField(default=True)),
                ('course', models.ForeignKey(verbose_name='Kurs', to='course.Course')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CourseMaterialUnit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('text', models.TextField(verbose_name='Text', blank=True)),
                ('status', models.CharField(default='0', max_length=2, choices=[('0', 'Im Aufbau'), ('1', 'Fertig')])),
                ('title', models.CharField(max_length=100, verbose_name='Ueberschrift')),
                ('display_nr', models.IntegerField(verbose_name='interne Nummer, steuert die Anzeigereihenfolge')),
                ('description', models.CharField(max_length=200, verbose_name='kurze Beschreibung', blank=True)),
                ('document_type', models.CharField(default='t', max_length=2, verbose_name='Anzeigemodus', choices=[('g', 'PDF Viewer'), ('1', 'PDF download und Text'), ('t', 'Text')])),
                ('slug', autoslug.fields.AutoSlugField(editable=False, blank=True)),
                ('file', models.FileField(upload_to=apps.course.models.lesson_material_name, verbose_name='Datei', blank=True)),
                ('sub_unit_nr', models.IntegerField(null=True, blank=True)),
                ('course', models.ForeignKey(verbose_name='Kurs', to='course.Course')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CourseOwner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('text', models.TextField(verbose_name='Text', blank=True)),
                ('status', models.CharField(default='0', max_length=2, choices=[('0', 'Im Aufbau'), ('1', 'Fertig')])),
                ('foto', models.ImageField(upload_to=foto_location, blank=True)),
                ('display', models.BooleanField(default=True, verbose_name='Anzeigen bei der Kursausschreibung?')),
                ('display_nr', models.IntegerField(default=1, verbose_name='Anzeigereihenfolge bei mehreren Kursleitern')),
                ('course', models.ForeignKey(to='course.Course')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CourseUnit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('text', models.TextField(verbose_name='Text', blank=True)),
                ('status', models.CharField(default='0', max_length=2, choices=[('0', 'Im Aufbau'), ('1', 'Fertig')])),
                ('title', models.CharField(max_length=100, verbose_name='Ueberschrift')),
                ('display_nr', models.IntegerField(verbose_name='interne Nummer, steuert die Anzeigereihenfolge')),
                ('description', models.CharField(max_length=200, verbose_name='kurze Beschreibung', blank=True)),
                ('unit_type', models.CharField(default='l', max_length=2, choices=[('o', 'Organisation'), ('l', 'Unterricht'), ('b', 'Bonusmaterial'), ('c', 'Klassenliste'), ('k', 'Kommunikation'), ('i', 'Intern'), ('s', 'Syllabus')])),
                ('unit_nr', models.IntegerField(null=True, verbose_name='Lektionsnummer', blank=True)),
                ('block', models.ForeignKey(default=1, verbose_name='Unterrichtsblock', to='course.CourseBlock')),
                ('course', models.ForeignKey(verbose_name='Kurs', to='course.Course')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='coursematerialunit',
            name='unit',
            field=models.ForeignKey(default=1, verbose_name='Lektion', to='course.CourseUnit'),
            preserve_default=True,
        ),
    ]
