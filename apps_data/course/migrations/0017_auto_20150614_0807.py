# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps_data.course.models.oldcoursepart


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0016_auto_20150610_1451'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='material',
            name='lesson',
        ),
        migrations.AddField(
            model_name='lesson',
            name='material',
            field=models.ManyToManyField(to='course.Material'),
        ),
        migrations.AlterField(
            model_name='course',
            name='prerequisites',
            field=models.TextField(verbose_name='Voraussetzungen', blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='project',
            field=models.TextField(verbose_name='Teilnehmerprojekt', blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='structure',
            field=models.TextField(verbose_name='Gliederung', blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='target_group',
            field=models.TextField(verbose_name='Zielgruppe', blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='text',
            field=models.TextField(verbose_name='Kursbeschreibung', blank=True),
        ),
        migrations.AlterField(
            model_name='coursematerialunit',
            name='file',
            field=models.FileField(upload_to=apps_data.course.models.oldcoursepart.lesson_material_name, verbose_name='Datei', blank=True),
        ),
    ]
