# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0045_auto_20150405_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursematerialunit',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='course.CourseUnit', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='courseunit',
            name='block',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='Unterrichtsblock', blank=True, to='course.CourseBlock', null=True),
            preserve_default=True,
        ),
    ]
