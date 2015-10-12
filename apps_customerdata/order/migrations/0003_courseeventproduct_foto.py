# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps_customerdata.mentoki_product.models.courseevent


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0002_auto_20150930_2243'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseeventproduct',
            name='foto',
            field=models.ImageField(help_text='Hier kannst Du ein Foto f\xfcr Deinen Kurs hochladen.',
                                    upload_to=apps_customerdata.mentoki_product.models.courseevent.foto_location, verbose_name='Foto', blank=True),
        ),
    ]
