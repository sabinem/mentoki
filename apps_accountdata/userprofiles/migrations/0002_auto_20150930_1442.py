# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings
import userprofiles.models.mentor


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentorsprofile',
            name='foto',
            field=models.ImageField(help_text='Hier kannst Du ein Foto von Dir hochladen.', upload_to=userprofiles.models.mentor.foto_location, verbose_name='Foto', blank=True),
        ),
        migrations.AlterField(
            model_name='mentorsprofile',
            name='text',
            field=models.TextField(help_text='Personenbeschreibung', verbose_name='Kursleiterbeschreibung', blank=True),
        ),
        migrations.AlterField(
            model_name='mentorsprofile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='Mentor', to=settings.AUTH_USER_MODEL),
        ),
    ]
