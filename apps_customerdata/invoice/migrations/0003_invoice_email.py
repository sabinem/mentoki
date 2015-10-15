# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0002_auto_20151014_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='email',
            field=models.EmailField(default='x', max_length=254),
            preserve_default=False,
        ),
    ]
