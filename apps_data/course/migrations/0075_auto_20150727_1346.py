# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields
import apps_data.course.models.oldcoursepart


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0074_auto_20150727_0815'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lessonpublisher',
            name='published_at',
        ),
        migrations.AddField(
            model_name='lessonpublisher',
            name='publish_status_changed',
            field=model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='published'),
        ),
        migrations.AlterField(
            model_name='coursematerialunit',
            name='file',
            field=models.FileField(upload_to=apps_data.course.models.oldcoursepart.lesson_material_name, verbose_name='Datei', blank=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='lesson_type',
            field=models.CharField(default='block', max_length=15, choices=[('block', 'Block'), ('lesson', 'Lesson'), ('step', 'Step')]),
        ),
    ]
