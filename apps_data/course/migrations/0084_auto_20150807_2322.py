# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
import apps_data.course.models.oldcoursepart
import model_utils.fields
import apps_data.course.models.material
import apps_core.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0083_auto_20150807_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursematerialunit',
            name='file',
            field=models.FileField(upload_to=apps_data.course.models.oldcoursepart.lesson_material_name, verbose_name='Datei', blank=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='description',
            field=models.CharField(help_text='Diese Beschreibung wird in Listen oder \xdcbersichtsseiten\n        angezeigt.', max_length=200, verbose_name='kurze Beschreibung des Materials', blank=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='document_type',
            field=model_utils.fields.StatusField(default='pdf', choices=[(0, 'dummy')], max_length=100, help_text='Derzeit sind nur pdf und zip erlaubt.', verbose_name='Dateityp', no_check_for_status=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='file',
            field=apps_core.core.fields.ContentTypeRestrictedFileField(upload_to=apps_data.course.models.material.lesson_material_name, verbose_name='Datei'),
        ),
        migrations.AlterField(
            model_name='material',
            name='pdf_download_link',
            field=models.BooleanField(default=False, help_text='Es wird ein Download-Link angeboten.', verbose_name='Download-Link anbieten?'),
        ),
        migrations.AlterField(
            model_name='material',
            name='pdf_link',
            field=models.BooleanField(default=False, help_text='Bei Dateityp pdf: das pdf-file ist \xfcber einen Link\n        erreichbar.', verbose_name='Link anbieten?'),
        ),
        migrations.AlterField(
            model_name='material',
            name='pdf_viewer',
            field=models.BooleanField(default=False, help_text='Bei Dateityp pdf: Das pdf-Datei ist durch einen Pdf-\n        Viewer ind die Webseite integriert, falls das m\xf6glich ist (auf dem PC\n        zum Beispiel).', verbose_name='Pdf-Viewer anbieten?'),
        ),
        migrations.AlterField(
            model_name='material',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='get_file_slug', always_update=True, unique=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='title',
            field=models.CharField(help_text='Titel, unter dem das Material angezeigt wird.\n        ', unique=True, max_length=100, verbose_name='Material-Titel'),
        ),
    ]
