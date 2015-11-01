# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0041_auto_20151029_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialoffer',
            name='course',
            field=models.OneToOneField(default=1, to='course.Course'),
            preserve_default=False,
        ),
    ]
