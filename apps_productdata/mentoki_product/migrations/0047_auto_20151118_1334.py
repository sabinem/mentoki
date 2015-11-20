# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0046_auto_20151115_2045'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseproductgroup',
            name='can_be_booked_now',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='courseproductgroup',
            name='published',
            field=models.BooleanField(default=False),
        ),
    ]
