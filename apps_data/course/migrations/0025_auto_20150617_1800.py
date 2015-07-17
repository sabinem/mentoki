# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps_data.course.models.oldcoursepart


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0024_auto_20150617_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='block',
            field=models.ForeignKey(blank=True, to='course.CourseBlock', null=True),
        ),
        migrations.AddField(
            model_name='lesson',
            name='unit',
            field=models.ForeignKey(blank=True, to='course.CourseUnit', null=True),
        ),
        migrations.AddField(
            model_name='lesson',
            name='unitmaterial',
            field=models.ForeignKey(blank=True, to='course.CourseMaterialUnit', null=True),
        ),
        migrations.AlterField(
            model_name='coursematerialunit',
            name='file',
            field=models.FileField(upload_to=apps_data.course.models.oldcoursepart.lesson_material_name, verbose_name='Datei', blank=True),
        ),
    ]
