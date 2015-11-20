# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textchunks', '0009_staticpublicpages'),
    ]

    operations = [
        migrations.DeleteModel(
            name='StaticPublicPages',
        ),
        migrations.AlterModelOptions(
            name='publictextchunks',
            options={'verbose_name': 'chunks', 'verbose_name_plural': 'chunks'},
        ),
    ]
