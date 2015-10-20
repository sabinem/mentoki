# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0022_auto_20151019_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseproductgroup',
            name='discount_text_long',
            field=models.CharField(default='', max_length=200, blank=True),
        ),
    ]
