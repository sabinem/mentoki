# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
import django.utils.timezone
from django.conf import settings
import model_utils.fields
import apps.course.models


class Migration(migrations.Migration):

    replaces = [(b'course', '0001_initial'), (b'course', '0002_auto_20141211_1526'), (b'course', '0003_courseowner_text'), (b'course', '0004_auto_20141211_1829'), (b'course', '0005_auto_20141212_1824'), (b'course', '0006_auto_20141215_0603'), (b'course', '0007_auto_20141217_0615'), (b'course', '0008_course_email'), (b'course', '0009_auto_20150105_1623'), (b'course', '0010_auto_20150105_1644'), (b'course', '0011_auto_20150105_2026'), (b'course', '0012_auto_20150106_2116'), (b'course', '0013_auto_20150112_1157'), (b'course', '0014_auto_20150123_1115'), (b'course', '0015_coursecomments'), (b'course', '0016_coursecomments_course'), (b'course', '0017_coursematerialunit_document'), (b'course', '0018_auto_20150124_1639'), (b'course', '0019_remove_coursematerialunit_document'), (b'course', '0020_coursematerialunit_document'), (b'course', '0021_auto_20150124_2228'), (b'course', '0022_coursematerial'), (b'course', '0023_auto_20150130_2221'), (b'course', '0024_auto_20150130_2233'), (b'course', '0025_courseunit_unit_type'), (b'course', '0026_auto_20150131_1314'), (b'course', '0027_auto_20150206_2114'), (b'course', '0028_auto_20150207_1548'), (b'course', '0029_auto_20150208_0125'), (b'course', '0030_auto_20150213_1644'), (b'course', '0031_auto_20150219_1026'), (b'course', '0032_auto_20150219_1035'), (b'course', '0034_auto_20150219_1251'), (b'course', '0035_auto_20150219_1336'), (b'course', '0036_auto_20150219_2133'), (b'course', '0037_auto_20150219_2146'), (b'course', '0038_auto_20150223_2234'), (b'course', '0039_auto_20150323_1408'), (b'course', '0040_auto_20150323_2145'), (b'course', '0041_auto_20150326_1133'), (b'course', '0042_auto_20150326_1150'), (b'course', '0043_auto_20150327_1115'), (b'course', '0044_courseowner_foto'), (b'course', '0045_auto_20150405_1710'), (b'course', '0046_auto_20150406_2133'), (b'course', '0047_auto_20150410_0808'), (b'course', '0048_courseblock_show_full'), (b'course', '0049_auto_20150410_1055'), (b'course', '0050_auto_20150410_1109'), (b'course', '0051_auto_20150411_2158'), (b'course', '0052_auto_20150413_1125'), (b'course', '0053_course_structure'), (b'course', '0054_auto_20150424_1029'), (b'course', '0055_auto_20150429_1608'), (b'course', '0056_auto_20150430_0650')]

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pdf', '__first__'),
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
