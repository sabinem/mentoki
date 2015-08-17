# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0002_auto_20150814_0703'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='classlesson',
            options={'verbose_name': 'Lektion (Kurs)', 'verbose_name_plural': 'Lektionen (Kurs)'},
        ),
        migrations.AlterModelOptions(
            name='lesson',
            options={'verbose_name': 'Lektion (Vorlage)', 'verbose_name_plural': 'Lektionen (Vorlage)'},
        ),
    ]
