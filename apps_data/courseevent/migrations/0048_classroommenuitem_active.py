# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0047_auto_20150817_1025'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroommenuitem',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
