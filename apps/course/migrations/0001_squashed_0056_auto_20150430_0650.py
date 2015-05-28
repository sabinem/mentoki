# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
import django.utils.timezone
from django.conf import settings
import model_utils.fields
import apps.course.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('slug', models.SlugField(unique=True)),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('excerpt', models.TextField()),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CourseMaterialUnit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('title', models.CharField(max_length=100, verbose_name=b'Ueberschrift')),
                ('text', models.TextField()),
                ('excerpt', models.TextField()),
                ('display_nr', models.IntegerField(verbose_name=b'interne Anzeigenummer: dient nur zum Ordnen, extern nicht sichtbar')),
                ('required', models.BooleanField(default=True)),
                ('course', models.ForeignKey(to='course.Course')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CourseOwner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('course', models.ForeignKey(to='course.Course')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('text', models.TextField(verbose_name='Text', blank=True)),
                ('status', models.CharField(default=b'0', max_length=2, choices=[(b'0', b'Im Aufbau'), (b'1', b'Fertig')])),
                ('foto', models.ImageField(upload_to=apps.course.models.course_name, blank=True)),
                ('display', models.BooleanField(default=True, verbose_name='Anzeigen bei der Kursausschreibung?')),
                ('display_nr', models.IntegerField(default=1, verbose_name='Anzeigereihenfolge bei mehreren Kursleitern')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CourseUnit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('title', models.CharField(max_length=100, verbose_name=b'Ueberschrift')),
                ('text', models.TextField(blank=True)),
                ('display_nr', models.IntegerField()),
                ('course', models.ForeignKey(to='course.Course')),
                ('unit_type', models.CharField(default=b'l', max_length=2, choices=[(b'o', b'Organisation'), (b'l', b'Unterricht'), (b'b', b'Bonusmaterial'), (b'c', b'Klassenliste'), (b'k', b'Kommunikation'), (b'i', b'Intern'), (b's', b'Syllabus')])),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='coursematerialunit',
            name='unit',
            field=models.ForeignKey(default=1, verbose_name='Lektion', to='course.CourseUnit'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='prerequisites',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='target_group',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='excerpt',
            field=models.TextField(default=b'text'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='text',
            field=models.TextField(default=b'text'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='excerpt',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='text',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coursematerialunit',
            name='display_nr',
            field=models.IntegerField(),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='coursematerialunit',
            name='excerpt',
        ),
        migrations.AddField(
            model_name='course',
            name='email',
            field=models.EmailField(default=b'info@netteachers.de', max_length=75),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coursematerialunit',
            name='text',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='coursematerialunit',
            name='required',
        ),
        migrations.AddField(
            model_name='coursematerialunit',
            name='document_type',
            field=models.CharField(default='t', max_length=2, verbose_name='Anzeigemodus', choices=[('g', 'PDF Viewer'), ('1', 'PDF download und Text'), ('t', 'Text')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='status',
            field=models.CharField(default=b'0', max_length=2, choices=[(b'0', b'Im Aufbau'), (b'1', b'Fertig')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='takeaway',
            field=models.TextField(default=b'x', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='coursematerialunit',
            name='file',
            field=models.FileField(upload_to=apps.course.models.lesson_material_name, verbose_name='Datei', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='coursematerialunit',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, blank=True),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='CourseBlock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('title', models.CharField(max_length=100, verbose_name=b'Ueberschrift')),
                ('text', models.TextField(verbose_name='Text', blank=True)),
                ('display_nr', models.IntegerField(verbose_name='interne Nummer, steuert die Anzeigereihenfolge')),
                ('is_numbered', models.BooleanField(default=True)),
                ('course', models.ForeignKey(verbose_name='Kurs', to='course.Course')),
                ('status', models.CharField(default=b'0', max_length=2, choices=[(b'0', b'Im Aufbau'), (b'1', b'Fertig')])),
                ('description', models.CharField(max_length=200, verbose_name='kurze Beschreibung', blank=True)),
                ('show_full', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='coursematerialunit',
            name='sub_unit_nr',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='courseunit',
            name='block',
            field=models.ForeignKey(default=1, verbose_name='Unterrichtsblock', to='course.CourseBlock'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='courseunit',
            name='unit_nr',
            field=models.IntegerField(null=True, verbose_name='Lektionsnummer', blank=True),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='course',
            name='status',
        ),
        migrations.AddField(
            model_name='coursematerialunit',
            name='status',
            field=models.CharField(default=b'0', max_length=2, choices=[(b'0', b'Im Aufbau'), (b'1', b'Fertig')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='courseunit',
            name='status',
            field=models.CharField(default=b'0', max_length=2, choices=[(b'0', b'Im Aufbau'), (b'1', b'Fertig')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='status',
            field=models.CharField(default=b'0', max_length=2, choices=[(b'0', b'Im Aufbau'), (b'1', b'Fertig')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(max_length=100, verbose_name=b'Ueberschrift'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='coursematerialunit',
            name='description',
            field=models.CharField(max_length=200, verbose_name='kurze Beschreibung', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='courseunit',
            name='description',
            field=models.CharField(max_length=200, verbose_name='kurze Beschreibung', blank=True),
            preserve_default=True,
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
            model_name='coursematerialunit',
            name='course',
            field=models.ForeignKey(verbose_name='Kurs', to='course.Course'),
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
            model_name='courseunit',
            name='course',
            field=models.ForeignKey(verbose_name='Kurs', to='course.Course'),
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
            model_name='course',
            name='text',
            field=models.TextField(verbose_name='Text', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coursematerialunit',
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
        migrations.AlterField(
            model_name='coursematerialunit',
            name='display_nr',
            field=models.IntegerField(verbose_name='interne Nummer, steuert die Anzeigereihenfolge', validators=[apps.course.models.validate_unique]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='courseunit',
            name='display_nr',
            field=models.IntegerField(verbose_name='interne Nummer, steuert die Anzeigereihenfolge', validators=[apps.course.models.validate_unique]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coursematerialunit',
            name='display_nr',
            field=models.IntegerField(verbose_name='interne Nummer, steuert die Anzeigereihenfolge'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='courseunit',
            name='display_nr',
            field=models.IntegerField(verbose_name='interne Nummer, steuert die Anzeigereihenfolge'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coursematerialunit',
            name='display_nr',
            field=models.IntegerField(verbose_name='Lektions-Nummer, steuert die Anzeigereihenfolge bei unnumerierten Unterrichtsbl\xf6cken'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='courseunit',
            name='display_nr',
            field=models.IntegerField(verbose_name='Lektions-Nummer, steuert die Anzeigereihenfolge bei unnumerierten Unterrichtsbl\xf6cken'),
            preserve_default=True,
        ),
        migrations.RenameField(
            model_name='course',
            old_name='takeaway',
            new_name='project',
        ),
        migrations.AlterField(
            model_name='coursematerialunit',
            name='display_nr',
            field=models.IntegerField(verbose_name='interne Nummer, steuert die Anzeigereihenfolge'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='courseunit',
            name='display_nr',
            field=models.IntegerField(verbose_name='interne Nummer, steuert die Anzeigereihenfolge'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='structure',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
