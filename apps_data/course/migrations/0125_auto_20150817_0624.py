# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps_data.course.models.oldcoursepart
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0124_auto_20150816_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursematerialunit',
            name='file',
            field=models.FileField(upload_to=apps_data.course.models.oldcoursepart.lesson_material_name, verbose_name='Datei', blank=True),
        ),
        migrations.AlterField(
            model_name='courseowner',
            name='course',
            field=models.ForeignKey(to='course.Course', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AlterField(
            model_name='courseowner',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='Kursleiter', to=settings.AUTH_USER_MODEL),
        ),
    ]
