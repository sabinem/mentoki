# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20141211_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseowner',
            name='text',
            field=models.TextField(default=b'text'),
            preserve_default=True,
        ),
    ]
