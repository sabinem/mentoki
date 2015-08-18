# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps_data.course.models.oldcoursepart
import model_utils.fields
import autoslug.fields
import mptt.fields
import django.utils.timezone
import apps_data.course.models.xmaterial


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20150605_2333'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentBlock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('title', models.CharField(max_length=100, verbose_name='Ueberschrift')),
                ('description', models.CharField(max_length=200, verbose_name='kurze Beschreibung', blank=True)),
                ('text', models.TextField(verbose_name='Beschreibung', blank=True)),
                ('status', models.TextField(verbose_name='Status', blank=True)),
            ],
            options={
                'verbose_name': 'Unterrichtsblock',
                'verbose_name_plural': 'Unterrichtsbl\xf6cke',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nr', models.IntegerField()),
                ('title', models.CharField(unique=True, max_length=50)),
                ('text', models.TextField()),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('block', models.ForeignKey(to='course.ContentBlock')),
            ],
            options={
                'verbose_name': 'Lektion',
                'verbose_name_plural': 'Lektionen',
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('document_type', model_utils.fields.StatusField(default='Text', max_length=100, no_check_for_status=True, choices=[('Text', 'Text'), ('PDF Viewer', 'PDF Viewer'), ('PDF download und Text', 'PDF download und Text')])),
                ('file', models.FileField(upload_to=apps_data.course.models.xmaterial.lesson_material_name, verbose_name='Datei', blank=True)),
                ('slug', autoslug.fields.AutoSlugField(populate_from='get_file_slug', editable=False, blank=True)),
            ],
            options={
                'verbose_name': 'Material',
                'verbose_name_plural': 'Materialien',
            },
        ),
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': 'Kursvorlage', 'verbose_name_plural': 'Kursvorlagen'},
        ),
        migrations.AlterModelOptions(
            name='courseblock',
            options={'ordering': ['display_nr'], 'verbose_name': 'XUnterrichtsblock', 'verbose_name_plural': 'XUnterrichtsbl\xf6cke'},
        ),
        migrations.AlterModelOptions(
            name='coursematerialunit',
            options={'verbose_name': 'xMaterial'},
        ),
        migrations.AlterModelOptions(
            name='courseowner',
            options={'ordering': ['course', 'display_nr'], 'verbose_name': 'Kursleitung', 'verbose_name_plural': 'Kursleitungen'},
        ),
        migrations.AlterModelOptions(
            name='courseunit',
            options={'verbose_name': 'xLektion'},
        ),
        migrations.RemoveField(
            model_name='course',
            name='status',
        ),
        migrations.RemoveField(
            model_name='coursematerialunit',
            name='sub_unit_nr',
        ),
        migrations.RemoveField(
            model_name='courseowner',
            name='status',
        ),
        migrations.RemoveField(
            model_name='courseunit',
            name='unit_nr',
        ),
        migrations.RemoveField(
            model_name='courseunit',
            name='unit_type',
        ),
        migrations.AlterField(
            model_name='course',
            name='email',
            field=models.EmailField(default='info@mentoki.com', max_length=254),
        ),
        migrations.AlterField(
            model_name='course',
            name='excerpt',
            field=models.TextField(verbose_name='Abstrakt', blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='project',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='title', blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='courseblock',
            name='course',
            field=models.ForeignKey(verbose_name='XKurs', to='course.Course'),
        ),
        migrations.AlterField(
            model_name='courseblock',
            name='status',
            field=model_utils.fields.StatusField(default='Entwurf', max_length=100, no_check_for_status=True, choices=[(0, 'dummy')]),
        ),
        migrations.AlterField(
            model_name='coursematerialunit',
            name='course',
            field=models.ForeignKey(verbose_name='XKurs', to='course.Course'),
        ),
        migrations.AlterField(
            model_name='coursematerialunit',
            name='document_type',
            field=model_utils.fields.StatusField(default='Text', max_length=100, no_check_for_status=True, choices=[(0, 'dummy')]),
        ),
        migrations.AlterField(
            model_name='coursematerialunit',
            name='file',
            field=models.FileField(upload_to=apps_data.course.models.oldcoursepart.lesson_material_name, verbose_name='Datei', blank=True),
        ),
        migrations.AlterField(
            model_name='coursematerialunit',
            name='status',
            field=model_utils.fields.StatusField(default='Entwurf', max_length=100, no_check_for_status=True, choices=[(0, 'dummy')]),
        ),
        migrations.AlterField(
            model_name='coursematerialunit',
            name='unit',
            field=models.ForeignKey(to='course.CourseUnit'),
        ),
        migrations.AlterField(
            model_name='courseunit',
            name='block',
            field=models.ForeignKey(to='course.CourseBlock'),
        ),
        migrations.AlterField(
            model_name='courseunit',
            name='course',
            field=models.ForeignKey(verbose_name='XKurs', to='course.Course'),
        ),
        migrations.AlterField(
            model_name='courseunit',
            name='status',
            field=model_utils.fields.StatusField(default='Entwurf', max_length=100, no_check_for_status=True, choices=[(0, 'dummy')]),
        ),
        migrations.AddField(
            model_name='material',
            name='course',
            field=models.ForeignKey(to='course.Course'),
        ),
        migrations.AddField(
            model_name='material',
            name='lesson',
            field=models.ManyToManyField(to='course.Lesson'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='course',
            field=models.ForeignKey(to='course.Course'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='parent',
            field=mptt.fields.TreeForeignKey(related_name='children', blank=True, to='course.Lesson', null=True),
        ),
        migrations.AddField(
            model_name='contentblock',
            name='course',
            field=models.ForeignKey(verbose_name='Kurs', to='course.Course'),
        ),
    ]
