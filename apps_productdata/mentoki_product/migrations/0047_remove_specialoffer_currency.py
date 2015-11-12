# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0046_remove_specialoffer_reach'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specialoffer',
            name='currency',
        ),
    ]
