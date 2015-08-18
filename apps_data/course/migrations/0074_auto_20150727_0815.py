# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields
import apps_data.course.models.oldcoursepart


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0024_auto_20150726_1808'),
        ('course', '0073_auto_20150726_1808'),
    ]

    operations = [
        migrations.CreateModel(
            name='LessonPublisher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('published_at', model_utils.fields.MonitorField(default=django.utils.timezone.now, when=set([True]), monitor='published')),
                ('published', models.BooleanField(default=False)),
                ('courseevent', models.ForeignKey(to='courseevent.CourseEvent')),
            ],
            options={
                'verbose_name': 'LessonPublisher',
            },
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='published',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='published_at',
        ),
        migrations.AddField(
            model_name='lesson',
            name='lesson_type',
            field=models.CharField(default='block', max_length=15, choices=[('block', 'Lesson Block'), ('lesson', 'Lesson'), ('step', 'Lesson Step')]),
        ),
        migrations.AlterField(
            model_name='coursematerialunit',
            name='file',
            field=models.FileField(upload_to=apps_data.course.models.oldcoursepart.lesson_material_name, verbose_name='Datei', blank=True),
        ),
        migrations.AddField(
            model_name='lessonpublisher',
            name='lesson',
            field=models.ForeignKey(to='course.Lesson'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='published_in_courseevent',
            field=models.ManyToManyField(to='courseevent.CourseEvent', through='course.LessonPublisher', blank=True),
        ),
    ]
