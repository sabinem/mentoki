# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0015_coursecomments'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursecomments',
            name='course',
            field=models.ForeignKey(default=1, to='course.Course'),
            preserve_default=True,
        ),
    ]
