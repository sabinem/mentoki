# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0010_auto_20160119_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classlesson',
            name='show_number',
            field=models.BooleanField(default=True, verbose_name='Nummerierung anzeigen'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='show_number',
            field=models.BooleanField(default=True, verbose_name='Nummerierung anzeigen'),
        ),
    ]
