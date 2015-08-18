# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0011_auto_20150724_0818'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='item_title',
            field=models.CharField(default='x', max_length=200),
        ),
    ]
