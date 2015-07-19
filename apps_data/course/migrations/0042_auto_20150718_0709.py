# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import apps_data.course.models.oldcoursepart


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0041_auto_20150717_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='owners',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='course.CourseOwner'),
        ),
        migrations.AlterField(
            model_name='coursematerialunit',
            name='file',
            field=models.FileField(upload_to=apps_data.course.models.oldcoursepart.lesson_material_name, verbose_name='Datei', blank=True),
        ),
    ]
