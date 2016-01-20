# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0009_auto_20160119_2053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classlesson',
            name='is_numbered',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='is_numbered',
        ),
        migrations.AddField(
            model_name='classlesson',
            name='show_number',
            field=models.BooleanField(default=True, help_text='Nummer als Lektions oder Abschnittsnummer anzeigen', verbose_name='Nummerierung anzeigen'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='show_number',
            field=models.BooleanField(default=True, help_text='Nummer als Lektions oder Abschnittsnummer anzeigen', verbose_name='Nummerierung anzeigen'),
        ),
    ]
