# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_auto_20151112_2203'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='currency',
            field=models.IntegerField(default=1),
        ),
    ]
