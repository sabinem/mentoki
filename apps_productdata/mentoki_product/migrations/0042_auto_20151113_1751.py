# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0041_courseproduct_nr_parts'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialoffer',
            name='courseproduct',
            field=models.ForeignKey(blank=True, to='mentoki_product.CourseProduct', null=True),
        ),
        migrations.AddField(
            model_name='specialoffer',
            name='courseproductgroup',
            field=models.ForeignKey(blank=True, to='mentoki_product.CourseProductGroup', null=True),
        ),
        migrations.AddField(
            model_name='specialoffer',
            name='courseproductsubgroup',
            field=models.ForeignKey(blank=True, to='mentoki_product.CourseProductSubGroup', null=True),
        ),
    ]
