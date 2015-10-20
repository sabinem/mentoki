# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_auto_20150929_1005'),
        ('mentoki_product', '0025_specialoffer_percentage_off'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialoffer',
            name='course',
            field=models.ForeignKey(blank=True, to='course.Course', null=True),
        ),
    ]
