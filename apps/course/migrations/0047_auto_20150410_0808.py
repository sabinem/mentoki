# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import apps.course.models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0046_auto_20150406_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='text',
            field=models.TextField(verbose_name='Text', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='courseblock',
            name='text',
            field=models.TextField(verbose_name='Text', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coursematerialunit',
            name='document_type',
            field=models.CharField(default='t', max_length=2, verbose_name='Anzeigemodus', choices=[('g', 'PDF Viewer'), ('1', 'PDF download und Text'), ('t', 'Text')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coursematerialunit',
            name='file',
            field=models.FileField(upload_to=apps.course.models.lesson_material_name, verbose_name='Datei', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coursematerialunit',
            name='text',
            field=models.TextField(verbose_name='Text', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coursematerialunit',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='Lektion', blank=True, to='course.CourseUnit', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='courseowner',
            name='text',
            field=models.TextField(verbose_name='Text', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='courseunit',
            name='text',
            field=models.TextField(verbose_name='Text', blank=True),
            preserve_default=True,
        ),
    ]
