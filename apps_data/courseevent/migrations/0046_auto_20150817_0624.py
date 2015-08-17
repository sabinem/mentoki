# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0045_courseeventlessonpublish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseevent',
            name='course',
            field=models.ForeignKey(to='course.Course', on_delete=django.db.models.deletion.PROTECT),
        ),
    ]
