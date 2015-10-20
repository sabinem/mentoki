# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0028_auto_20151019_1545'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specialoffer',
            name='offer_for_course',
        ),
        migrations.AlterField(
            model_name='specialoffer',
            name='courseproduct',
            field=models.OneToOneField(null=True, blank=True, to='mentoki_product.CourseProduct'),
        ),
    ]
