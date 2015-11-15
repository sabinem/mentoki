# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0038_auto_20151113_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseproduct',
            name='courseproductsubgroup',
            field=models.ForeignKey(default=1, to='mentoki_product.CourseProductSubGroup'),
        ),
    ]
