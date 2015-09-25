# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0006_auto_20150916_2202'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseevent',
            name='email_greeting',
            field=models.CharField(default='hallo', max_length=200),
            preserve_default=False,
        ),
    ]
