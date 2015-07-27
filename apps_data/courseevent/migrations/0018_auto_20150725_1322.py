# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courseevent', '0017_auto_20150725_1246'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentswork',
            name='user',
        ),
        migrations.AddField(
            model_name='studentswork',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
