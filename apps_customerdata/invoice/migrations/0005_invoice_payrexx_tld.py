# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0004_auto_20151014_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='payrexx_tld',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
