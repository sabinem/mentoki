# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0001_initial'),
        ('courseevent', '0039_auto_20150813_1100'),
        ('course', '0118_auto_20150813_1100'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassLesson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('nr', models.IntegerField(default=1, verbose_name='Nr.')),
                ('lesson_nr', models.CharField(help_text='abgeleitetes Feld: keine manuelle Eingabe', max_length=10, verbose_name='Lektionsnr.', blank=True)),
                ('title', models.CharField(help_text='Lektions-Titel', max_length=100, verbose_name='\xdcberschrift')),
                ('text', models.TextField(help_text='Text der Lektion', verbose_name='Lektionstext', blank=True)),
                ('description', models.CharField(help_text='diese Beschreibung erscheint nur in den \xdcbersichten', max_length=200, verbose_name='kurze Beschreibung', blank=True)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('course', models.ForeignKey(to='course.Course')),
                ('courseevent', models.ForeignKey(to='courseevent.CourseEvent')),
                ('materials', models.ManyToManyField(help_text='Material der Lektion', to='material.Material', verbose_name='Kursmaterial', blank=True)),
            ],
            options={
                'verbose_name': 'Kurs-Lektion',
                'verbose_name_plural': 'Kurs-Lektionen',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('nr', models.IntegerField(default=1, verbose_name='Nr.')),
                ('lesson_nr', models.CharField(help_text='abgeleitetes Feld: keine manuelle Eingabe', max_length=10, verbose_name='Lektionsnr.', blank=True)),
                ('title', models.CharField(help_text='Lektions-Titel', max_length=100, verbose_name='\xdcberschrift')),
                ('text', models.TextField(help_text='Text der Lektion', verbose_name='Lektionstext', blank=True)),
                ('description', models.CharField(help_text='diese Beschreibung erscheint nur in den \xdcbersichten', max_length=200, verbose_name='kurze Beschreibung', blank=True)),
                ('old_pk', models.IntegerField(null=True)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('course', models.ForeignKey(to='course.Course')),
                ('materials', models.ManyToManyField(help_text='Material der Lektion', to='material.Material', verbose_name='Kursmaterial', blank=True)),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', verbose_name='einh\xe4ngen unter', blank=True, to='lesson.Lesson', null=True)),
            ],
            options={
                'verbose_name': 'Vorlage-Lektion',
                'verbose_name_plural': 'Vorlage-Lektionen',
            },
        ),
        migrations.AddField(
            model_name='classlesson',
            name='original_lesson',
            field=models.ForeignKey(to='lesson.Lesson'),
        ),
        migrations.AddField(
            model_name='classlesson',
            name='parent',
            field=mptt.fields.TreeForeignKey(related_name='children', verbose_name='einh\xe4ngen unter', blank=True, to='lesson.ClassLesson', null=True),
        ),
    ]
