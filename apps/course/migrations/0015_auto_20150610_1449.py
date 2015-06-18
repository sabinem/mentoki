# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.course.models.oldcoursepart
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0014_auto_20150610_1422'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='document_type',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='file',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='pdf_download_link',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='pdf_link',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='pdf_viewer',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='slug',
        ),
        migrations.AddField(
            model_name='material',
            name='pdf_download_link',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='material',
            name='pdf_link',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='material',
            name='pdf_viewer',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='coursematerialunit',
            name='file',
            field=models.FileField(upload_to=apps.course.models.oldcoursepart.lesson_material_name, verbose_name='Datei', blank=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='document_type',
            field=model_utils.fields.StatusField(default='text', max_length=100, no_check_for_status=True, choices=[(0, 'dummy')]),
        ),
    ]
