# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import mptt.fields
import model_utils.fields
import django.utils.timezone
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0001_initial'),
        ('courseevent', '0001_initial'),
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassLesson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nr', models.IntegerField(default=1, verbose_name='Nr.')),
                ('lesson_nr', models.CharField(help_text='abgeleitetes Feld: keine manuelle Eingabe', verbose_name='Lektionsnr.', max_length=10, editable=False, blank=True)),
                ('title', models.CharField(help_text='Lektions-Titel', max_length=100, verbose_name='\xdcberschrift')),
                ('text', models.TextField(help_text='Text der Lektion', verbose_name='Lektionstext', blank=True)),
                ('description', models.CharField(help_text='diese Beschreibung erscheint nur in den \xdcbersichten', max_length=200, verbose_name='kurze Beschreibung', blank=True)),
                ('is_homework', models.BooleanField(default=False)),
                ('is_original_lesson', models.BooleanField(default=True)),
                ('due_date', models.DateField(null=True, verbose_name='Abgabedatum', blank=True)),
                ('extra_text', models.TextField(help_text='Anhang zu Aufgaben', verbose_name='Anhang Aufgabe', blank=True)),
                ('created', models.DateTimeField(default=datetime.datetime.now)),
                ('modified', models.DateTimeField(default=datetime.datetime.now)),
                ('published', models.BooleanField(default=False, verbose_name='ver\xf6ffentlicht', editable=False)),
                ('publish_status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='published')),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('course', models.ForeignKey(to='course.Course', on_delete=django.db.models.deletion.PROTECT)),
                ('courseevent', models.ForeignKey(to='courseevent.CourseEvent')),
                ('material', models.ForeignKey(blank=True, to='material.Material', help_text='Material der Lektion', null=True, verbose_name='Kursmaterial')),
            ],
            options={
                'verbose_name': 'Lektion (Kurs)',
                'verbose_name_plural': 'Lektionen (Kurs)',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('nr', models.IntegerField(default=1, verbose_name='Nr.')),
                ('lesson_nr', models.CharField(help_text='abgeleitetes Feld: keine manuelle Eingabe', verbose_name='Lektionsnr.', max_length=10, editable=False, blank=True)),
                ('title', models.CharField(help_text='Lektions-Titel', max_length=100, verbose_name='\xdcberschrift')),
                ('text', models.TextField(help_text='Text der Lektion', verbose_name='Lektionstext', blank=True)),
                ('description', models.CharField(help_text='diese Beschreibung erscheint nur in den \xdcbersichten', max_length=200, verbose_name='kurze Beschreibung', blank=True)),
                ('is_homework', models.BooleanField(default=False)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('course', models.ForeignKey(to='course.Course', on_delete=django.db.models.deletion.PROTECT)),
                ('material', models.ForeignKey(blank=True, to='material.Material', help_text='Material der Lektion', null=True, verbose_name='Kursmaterial')),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', verbose_name='einh\xe4ngen unter', blank=True, to='lesson.Lesson', null=True)),
            ],
            options={
                'verbose_name': 'Lektion (Vorlage)',
                'verbose_name_plural': 'Lektionen (Vorlage)',
            },
        ),
        migrations.AddField(
            model_name='classlesson',
            name='original_lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='lesson.Lesson', null=True),
        ),
        migrations.AddField(
            model_name='classlesson',
            name='parent',
            field=mptt.fields.TreeForeignKey(related_name='children', verbose_name='einh\xe4ngen unter', blank=True, to='lesson.ClassLesson', null=True),
        ),
    ]
