# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.course.models.oldcoursepart


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0026_auto_20150618_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='unitmaterial',
            field=models.ForeignKey(blank=True, to='course.CourseMaterialUnit', null=True),
        ),
        migrations.AlterField(
            model_name='coursematerialunit',
            name='file',
            field=models.FileField(upload_to=apps.course.models.oldcoursepart.lesson_material_name, verbose_name='Datei', blank=True),
        ),
    ]
