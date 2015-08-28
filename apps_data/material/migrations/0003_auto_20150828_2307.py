# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0002_remove_material_pdf_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='pdf_download_link',
            field=models.BooleanField(default=True, help_text='Es wird ein Download-Link angeboten.', verbose_name='Download-Link anbieten?'),
        ),
        migrations.AlterField(
            model_name='material',
            name='pdf_viewer',
            field=models.BooleanField(default=True, help_text='Bei Dateityp pdf: Das pdf-Datei ist durch einen Pdf-\n        Viewer ind die Webseite integriert, falls das m\xf6glich ist (auf dem PC\n        zum Beispiel).', verbose_name='Pdf-Viewer anbieten?'),
        ),
    ]
