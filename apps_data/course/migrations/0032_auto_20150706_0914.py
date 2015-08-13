# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps_data.course.models.oldcoursepart
import apps_data.course.models.xmaterial


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0031_auto_20150705_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursematerialunit',
            name='file',
            field=models.FileField(upload_to=apps_data.course.models.oldcoursepart.lesson_material_name, verbose_name='Datei', blank=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='file',
            field=apps_data.course.models.xmaterial.ContentTypeRestrictedFileField(upload_to=apps_data.course.models.xmaterial.lesson_material_name, verbose_name='Datei', blank=True),
        ),
    ]
