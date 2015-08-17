# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0123_auto_20150816_1550'),
        ('material', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='unitmaterial',
            field=models.ForeignKey(blank=True, to='course.CourseMaterialUnit', null=True),
        ),
    ]
