# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps_data.course.models.course
import apps_data.course.models.oldcoursepart


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0091_auto_20150809_2008'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson',
            old_name='material',
            new_name='materials',
        ),
        migrations.AlterField(
            model_name='course',
            name='email',
            field=models.EmailField(default=b'info@mentoki.com', help_text='email des Kursleiters', max_length=254, verbose_name='email Addresse f\xfcr den Kurs'),
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
            model_name='coursematerialunit',
            name='file',
            field=models.FileField(upload_to=apps_data.course.models.oldcoursepart.lesson_material_name, verbose_name='Datei', blank=True),
        ),
        migrations.AlterField(
            model_name='courseowner',
            name='foto',
            field=models.ImageField(help_text='Hier kannst Du ein Foto von Dir hochladen, das auf der Kursauschreibung\n        erscheinen soll.', upload_to=apps_data.course.models.course.foto_location, verbose_name='Foto', blank=True),
        ),
        migrations.AlterField(
            model_name='courseowner',
            name='text',
            field=models.TextField(help_text='Personenbeschreibung: was qualifiziert Dich f\xfcr das Halten dieses\n        Kurses?', verbose_name='Text', blank=True),
        ),
    ]
