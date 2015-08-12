# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
import apps_data.material.models.material
import django.utils.timezone
import model_utils.fields
import apps_core.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0099_auto_20150812_1438'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('title', models.CharField(help_text='Titel, unter dem das Material angezeigt wird.\n        ', max_length=100, verbose_name='Material-Titel')),
                ('description', models.CharField(help_text='Diese Beschreibung wird in Listen oder \xdcbersichtsseiten\n        angezeigt.', max_length=200, verbose_name='kurze Beschreibung des Materials', blank=True)),
                ('document_type', model_utils.fields.StatusField(default='pdf', choices=[('zip', 'zip-Datei'), ('pdf', 'pdf-Datei')], max_length=100, help_text='Derzeit sind nur pdf und zip erlaubt.', verbose_name='Dateityp', no_check_for_status=True)),
                ('pdf_download_link', models.BooleanField(default=False, help_text='Es wird ein Download-Link angeboten.', verbose_name='Download-Link anbieten?')),
                ('pdf_viewer', models.BooleanField(default=False, help_text='Bei Dateityp pdf: Das pdf-Datei ist durch einen Pdf-\n        Viewer ind die Webseite integriert, falls das m\xf6glich ist (auf dem PC\n        zum Beispiel).', verbose_name='Pdf-Viewer anbieten?')),
                ('pdf_link', models.BooleanField(default=False, help_text='Bei Dateityp pdf: das pdf-file ist \xfcber einen Link\n        erreichbar.', verbose_name='Link anbieten?')),
                ('file', apps_core.core.fields.ContentTypeRestrictedFileField(upload_to=apps_data.material.models.material.lesson_material_name, verbose_name='Datei')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='get_file_slug', always_update=True, unique=True)),
                ('course', models.ForeignKey(related_name='coursematerial', to='course.Course')),
            ],
            options={
                'verbose_name': 'Material',
                'verbose_name_plural': 'Materialien',
            },
        ),
    ]
