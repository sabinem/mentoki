# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.course.models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0044_courseowner_foto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursematerialunit',
            name='document',
        ),
        migrations.AlterField(
            model_name='course',
            name='text',
            field=models.TextField(verbose_name='Lang-Text', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(max_length=100, verbose_name='\xdcberschrift'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='courseblock',
            name='course',
            field=models.ForeignKey(verbose_name='Kurs', to='course.Course'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='courseblock',
            name='description',
            field=models.CharField(max_length=200, verbose_name='kurze Beschreibung', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='courseblock',
            name='display_nr',
            field=models.IntegerField(verbose_name='interne Nummer, steuert die Anzeigereihenfolge'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='courseblock',
            name='text',
            field=models.TextField(verbose_name='Lang-Text', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coursematerialunit',
            name='course',
            field=models.ForeignKey(verbose_name='Kurs', to='course.Course'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coursematerialunit',
            name='description',
            field=models.CharField(max_length=200, verbose_name='kurze Beschreibung', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coursematerialunit',
            name='display_nr',
            field=models.IntegerField(verbose_name='interne Nummer, steuert die Anzeigereihenfolge'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coursematerialunit',
            name='text',
            field=models.TextField(verbose_name='Lang-Text', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='courseowner',
            name='foto',
            field=models.ImageField(upload_to=apps.course.models.course_name, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='courseowner',
            name='text',
            field=models.TextField(verbose_name='Lang-Text', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='courseunit',
            name='block',
            field=models.ForeignKey(verbose_name='Unterrichtsblock', blank=True, to='course.CourseBlock', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='courseunit',
            name='course',
            field=models.ForeignKey(verbose_name='Kurs', to='course.Course'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='courseunit',
            name='description',
            field=models.CharField(max_length=200, verbose_name='kurze Beschreibung', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='courseunit',
            name='display_nr',
            field=models.IntegerField(verbose_name='interne Nummer, steuert die Anzeigereihenfolge'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='courseunit',
            name='text',
            field=models.TextField(verbose_name='Lang-Text', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='courseunit',
            name='unit_nr',
            field=models.IntegerField(null=True, verbose_name='Lektionsnummer', blank=True),
            preserve_default=True,
        ),
    ]
