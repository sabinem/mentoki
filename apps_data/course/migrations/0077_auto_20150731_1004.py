# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps_data.course.models.oldcoursepart


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0076_auto_20150727_1347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='lesson_type',
        ),
        migrations.AlterField(
            model_name='course',
            name='target_group',
            field=models.TextField(help_text='The target group for your course.', verbose_name='target group', blank=True),
        ),
        migrations.AlterField(
            model_name='coursematerialunit',
            name='file',
            field=models.FileField(upload_to=apps_data.course.models.oldcoursepart.lesson_material_name, verbose_name='Datei', blank=True),
        ),
    ]
