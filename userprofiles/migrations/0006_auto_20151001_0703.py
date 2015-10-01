# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import userprofiles.models.mentor


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0005_auto_20150930_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentorsprofile',
            name='foto_detail_page',
            field=models.ImageField(help_text='Hier kannst Du ein Foto von Dir hochladen.\n                    Dieses Foto ist f\xfcr die Detailseite gedacht', upload_to=userprofiles.models.mentor.foto_location, verbose_name='Foto', blank=True),
        ),
        migrations.AlterField(
            model_name='mentorsprofile',
            name='foto',
            field=models.ImageField(help_text='Hier kannst Du ein Foto von Dir hochladen.\n                     Dieses Foto ist f\xfcr die Listenansicht gedacht', upload_to=userprofiles.models.mentor.foto_location, verbose_name='Foto', blank=True),
        ),
    ]
