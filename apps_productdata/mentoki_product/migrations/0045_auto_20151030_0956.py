# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0044_auto_20151029_1952'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseproductpart',
            name='course',
        ),
        migrations.RemoveField(
            model_name='courseproductpart',
            name='courseevent',
        ),
        migrations.RemoveField(
            model_name='courseproductpart',
            name='dependencies',
        ),
        migrations.RemoveField(
            model_name='courseproductpart',
            name='product_type',
        ),
        migrations.RenameField(
            model_name='producttype',
            old_name='belongs_to_courseevent',
            new_name='is_courseevent_participation',
        ),
        migrations.DeleteModel(
            name='CourseProductPart',
        ),
    ]
