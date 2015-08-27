# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0010_auto_20150826_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroommenuitem',
            name='optional',
            field=models.BooleanField(default=True),
        ),
    ]
