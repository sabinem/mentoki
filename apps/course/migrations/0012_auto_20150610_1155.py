# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.course.models.oldcoursepart
import django_filepicker.models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0011_auto_20150609_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='fpfile',
            field=django_filepicker.models.FPFileField(default='x', upload_to='uploads'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='coursematerialunit',
            name='file',
            field=models.FileField(upload_to=apps.course.models.oldcoursepart.lesson_material_name, verbose_name='Datei', blank=True),
        ),
    ]
