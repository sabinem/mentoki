# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0005_auto_20150817_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classlesson',
            name='published',
            field=models.BooleanField(default=False, verbose_name='ver\xf6ffentlicht', editable=False),
        ),
    ]
