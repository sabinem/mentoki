# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0019_auto_20150725_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentswork',
            name='workers',
            field=models.ManyToManyField(related_name='teammembers', to=settings.AUTH_USER_MODEL),
        ),
    ]
