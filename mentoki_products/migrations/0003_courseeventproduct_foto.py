# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mentoki_products.models.courseeventproduct


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_products', '0002_auto_20150930_2243'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseeventproduct',
            name='foto',
            field=models.ImageField(help_text='Hier kannst Du ein Foto f\xfcr Deinen Kurs hochladen.', upload_to=mentoki_products.models.courseeventproduct.foto_location, verbose_name='Foto', blank=True),
        ),
    ]
