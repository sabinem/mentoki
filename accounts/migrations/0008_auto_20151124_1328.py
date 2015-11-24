# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20151119_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='start_desk',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(upload_to=b'uploads', null=True, verbose_name=b'Profilbild', blank=True),
        ),
    ]
