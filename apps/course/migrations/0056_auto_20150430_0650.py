# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0055_auto_20150429_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursematerialunit',
            name='unit',
            field=models.ForeignKey(default=1, verbose_name='Lektion', to='course.CourseUnit'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='courseunit',
            name='block',
            field=models.ForeignKey(default=1, verbose_name='Unterrichtsblock', to='course.CourseBlock'),
            preserve_default=True,
        ),
    ]
