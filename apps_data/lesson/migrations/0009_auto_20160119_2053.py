# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0008_auto_20160119_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classlesson',
            name='is_numbered',
            field=models.BooleanField(default=True, help_text='Lektionen sind numeriert', verbose_name='nummerierter Block'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='is_numbered',
            field=models.BooleanField(default=True, help_text='Lektionen sind numeriert', verbose_name='nummerierter Block'),
        ),
    ]
