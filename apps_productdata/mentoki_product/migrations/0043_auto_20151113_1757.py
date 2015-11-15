# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0042_auto_20151113_1751'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseproductpart',
            name='course',
        ),
        migrations.RemoveField(
            model_name='courseproductpart',
            name='courseproduct',
        ),
        migrations.DeleteModel(
            name='CourseProductPart',
        ),
    ]
