# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps_data.course.models.oldcoursepart
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0030_auto_20150622_0706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursematerialunit',
            name='file',
            field=models.FileField(upload_to=apps_data.course.models.oldcoursepart.lesson_material_name, verbose_name='Datei', blank=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='document_type',
            field=model_utils.fields.StatusField(default='pdf', max_length=100, no_check_for_status=True, choices=[(0, 'dummy')]),
        ),
    ]
