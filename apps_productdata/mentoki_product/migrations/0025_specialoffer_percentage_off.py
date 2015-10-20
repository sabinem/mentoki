# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0024_courseproduct_display_nr'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialoffer',
            name='percentage_off',
            field=models.IntegerField(default=0),
        ),
    ]
