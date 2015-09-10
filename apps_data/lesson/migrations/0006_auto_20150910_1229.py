# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0005_auto_20150905_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='classlesson',
            name='block_sort',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='lesson',
            name='block_sort',
            field=models.IntegerField(default=1),
        ),
    ]
