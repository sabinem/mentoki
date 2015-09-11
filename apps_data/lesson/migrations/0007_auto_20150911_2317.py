# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0006_auto_20150910_1229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classlesson',
            name='block_sort',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='block_sort',
        ),
    ]
