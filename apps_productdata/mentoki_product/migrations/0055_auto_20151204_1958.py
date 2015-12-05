# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0054_courseproductgroupfield'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseproductgroupfield',
            name='course',
            field=models.ForeignKey(to='course.Course'),
        ),
    ]
