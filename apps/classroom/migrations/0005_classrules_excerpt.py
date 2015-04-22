# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0004_auto_20150102_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='classrules',
            name='excerpt',
            field=models.TextField(default=b'x'),
            preserve_default=True,
        ),
    ]
