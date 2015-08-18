# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps_data.course.models.oldcoursepart


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0055_auto_20150719_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='excerpt',
            field=models.TextField(help_text='Abstracts serve to describe courses on course list page', verbose_name='abstract', blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='prerequisites',
            field=models.TextField(help_text='The prequisites for your course. What prior knowledge must be there?', verbose_name='Voraussetzungen', blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='project',
            field=models.TextField(help_text='What do the participants take away from your course?', verbose_name='Teilnehmerprojekt', blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='structure',
            field=models.TextField(help_text='Provide the structure of your course.', verbose_name='Gliederung', blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='target_group',
            field=models.TextField(help_text='The target group for your course.', verbose_name='targetgroup', blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='text',
            field=models.TextField(help_text='Here you can give a detailed description of your course.', verbose_name='Kursbeschreibung', blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(help_text='Working title for your course. You may change this later on', max_length=100, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='coursematerialunit',
            name='file',
            field=models.FileField(upload_to=apps_data.course.models.oldcoursepart.lesson_material_name, verbose_name='Datei', blank=True),
        ),
    ]
