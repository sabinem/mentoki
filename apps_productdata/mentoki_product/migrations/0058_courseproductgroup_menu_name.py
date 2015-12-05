# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0057_auto_20151204_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseproductgroup',
            name='menu_name',
            field=models.CharField(default='x', max_length=100),
            preserve_default=False,
        ),
    ]
