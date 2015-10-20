# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textchunks', '0005_publictextchunks_banner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='publictextchunks',
            options={'verbose_name': 'Text f\xfcr Webseite', 'verbose_name_plural': 'Texte f\xfcr Webseite'},
        ),
    ]
