# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0043_auto_20151029_1858'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='courseproduct',
            options={'verbose_name': 'Kursangebote', 'verbose_name_plural': 'Kursangebote'},
        ),
        migrations.RenameField(
            model_name='producttype',
            old_name='is_courseevent',
            new_name='belongs_to_courseevent',
        ),
        migrations.RenameField(
            model_name='producttype',
            old_name='is_courseevent_part',
            new_name='is_part',
        ),
    ]
