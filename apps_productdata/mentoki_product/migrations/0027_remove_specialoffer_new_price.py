# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0026_specialoffer_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specialoffer',
            name='new_price',
        ),
    ]
