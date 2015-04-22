# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0023_auto_20150130_2221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursematerial',
            name='course',
        ),
        migrations.RemoveField(
            model_name='coursematerial',
            name='document',
        ),
        migrations.RemoveField(
            model_name='coursematerial',
            name='unit',
        ),
        migrations.DeleteModel(
            name='CourseMaterial',
        ),
    ]
