# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps_data.course.models.oldcoursepart


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0042_auto_20150718_0709'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='author',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='author',
        ),
        migrations.RemoveField(
            model_name='material',
            name='author',
        ),
        migrations.AlterField(
            model_name='coursematerialunit',
            name='file',
            field=models.FileField(upload_to=apps_data.course.models.oldcoursepart.lesson_material_name, verbose_name='Datei', blank=True),
        ),
    ]
