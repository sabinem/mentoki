# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0041_auto_20151106_1721'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseproduct',
            name='invoice_descriptor',
        ),
        migrations.RemoveField(
            model_name='courseproduct',
            name='product_typex',
        ),
        migrations.RemoveField(
            model_name='specialoffer',
            name='courseevent',
        ),
        migrations.RemoveField(
            model_name='specialoffer',
            name='courseproduct',
        ),
        migrations.AddField(
            model_name='specialoffer',
            name='currency',
            field=models.IntegerField(default=1),
        ),
    ]
