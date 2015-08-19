# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
import apps_data.course.models.oldcoursepart
import apps_data.course.models.course
import django.db.models.deletion
from django.conf import settings
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0002_auto_20150605_2333'),
    ]

    operations = [
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
        migrations.AddField(
            model_name='course',
            name='owners',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='course.CourseOwner'),
        ),
        migrations.AlterField(
            model_name='course',
            name='email',
            field=models.EmailField(default='info@mentoki.com', help_text='email des Kursleiters', max_length=254, verbose_name='email Addresse f\xfcr den Kurs'),
        ),
        migrations.AlterField(
            model_name='course',
            name='excerpt',
            field=models.TextField(help_text='Diese Kurzbeschreibung dient sp\xe4ter als Vorlage\n        bei der Ausschreibung Deiner Kurse', verbose_name='Kurze Zusammenfassung / Abstrakt', blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='prerequisites',
            field=models.TextField(help_text='Welches Vorwissen wird in Deinem\n        Kurses Voraussetzung?', verbose_name='Voraussetzungen', blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='project',
            field=models.TextField(help_text='What do the participants take away from your course?', verbose_name='Teilnehmerprojekt', blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=autoslug.fields.AutoSlugField(populate_from='title', unique=True, editable=False),
        ),
        migrations.AlterField(
            model_name='course',
            name='structure',
            field=models.TextField(help_text='Provide the structure of your course.', verbose_name='Gliederung', blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='target_group',
            field=models.TextField(help_text='Die Zielgruppe f\xfcr Deinen Kurs.', verbose_name='Zielgruppe', blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='text',
            field=models.TextField(help_text='Here you can give a detailed description of your course.', verbose_name='Kursbeschreibung', blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(help_text='Arbeitstitel f\xfcr Deinen Kurs. Er ist nicht \xf6ffentlich sichtbar.', max_length=100, verbose_name='Kurstitel'),
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
            model_name='courseowner',
            name='course',
            field=models.ForeignKey(to='course.Course', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AlterField(
            model_name='courseowner',
            name='display',
            field=models.BooleanField(default=True, help_text='Soll dieses Profil auf der Kursausschreibungsseite angezeigt werden?.', verbose_name='Anzeigen auf der Auschreibungsseite?'),
        ),
        migrations.AlterField(
            model_name='courseowner',
            name='display_nr',
            field=models.IntegerField(default=1, help_text='Dieses Feld steuert die Anzeigereihenfolge bei mehreren Kursleitern.', verbose_name='Anzeigereihenfolge'),
        ),
        migrations.AlterField(
            model_name='courseowner',
            name='foto',
            field=models.ImageField(help_text='Hier kannst Du ein Foto von Dir hochladen, das auf der Kursauschreibung\n        erscheinen soll.', upload_to=apps_data.course.models.course.foto_location, verbose_name='Kursleiter-Foto', blank=True),
        ),
        migrations.AlterField(
            model_name='courseowner',
            name='text',
            field=models.TextField(help_text='Personenbeschreibung: was qualifiziert Dich f\xfcr das Halten dieses\n        Kurses?', verbose_name='Kursleiterbeschreibung', blank=True),
        ),
        migrations.AlterField(
            model_name='courseowner',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='Kursleiter', to=settings.AUTH_USER_MODEL),
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
    ]
