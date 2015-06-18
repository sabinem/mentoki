# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
import apps.course.models.oldcoursepart
import apps.course.models.lesson
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_auto_20150608_1233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='block',
        ),
        migrations.AddField(
            model_name='lesson',
            name='document_type',
            field=model_utils.fields.StatusField(default='Text', max_length=100, no_check_for_status=True, choices=[(0, 'dummy')]),
        ),
        migrations.AddField(
            model_name='lesson',
            name='file',
            field=models.FileField(upload_to=apps.course.models.lesson.lesson_material_name, verbose_name='Datei', blank=True),
        ),
        migrations.AddField(
            model_name='lesson',
            name='slug',
            field=autoslug.fields.AutoSlugField(populate_from='get_file_slug', editable=False, blank=True),
        ),
        migrations.AlterField(
            model_name='coursematerialunit',
            name='file',
            field=models.FileField(upload_to=apps.course.models.oldcoursepart.lesson_material_name, verbose_name='Datei', blank=True),
        ),
    ]
