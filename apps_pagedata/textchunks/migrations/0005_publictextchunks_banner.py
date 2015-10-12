# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import apps_pagedata.textchunks.models


class Migration(migrations.Migration):

    dependencies = [
        ('textchunks', '0004_auto_20151012_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='publictextchunks',
            name='banner',
            field=models.ImageField(help_text='Hier kannst Du ein Foto f\xfcr Deinen Kurs hochladen.', upload_to=apps_pagedata.textchunks.models.foto_location, verbose_name='Banner', blank=True),
        ),
    ]
