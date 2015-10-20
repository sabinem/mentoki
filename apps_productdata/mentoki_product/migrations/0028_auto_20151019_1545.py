# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0027_remove_specialoffer_new_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialoffer',
            name='offer_for_course',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='specialoffer',
            name='courseproduct',
            field=models.ForeignKey(blank=True, to='mentoki_product.CourseProduct', null=True),
        ),
    ]
