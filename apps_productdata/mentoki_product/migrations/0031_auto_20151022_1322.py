# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0030_courseproductgroup_display_nr'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseproduct',
            name='meta_description',
            field=models.CharField(default='x', max_length=200),
        ),
        migrations.AddField(
            model_name='courseproduct',
            name='meta_keywords',
            field=models.CharField(default='x', max_length=200),
        ),
        migrations.AddField(
            model_name='courseproduct',
            name='meta_title',
            field=models.CharField(default='x', max_length=100),
        ),
    ]
