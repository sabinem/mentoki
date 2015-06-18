# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.course.models.oldcoursepart
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0019_auto_20150615_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursematerialunit',
            name='file',
            field=models.FileField(upload_to=apps.course.models.oldcoursepart.lesson_material_name, verbose_name='Datei', blank=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='material',
            field=models.ManyToManyField(to='course.Material', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='nr',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='parent',
            field=mptt.fields.TreeForeignKey(related_name='children', verbose_name='einh\xe4ngen unter', blank=True, to='course.Lesson', null=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
