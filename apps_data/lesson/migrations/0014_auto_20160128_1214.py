# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courseevent', '0023_auto_20160119_2041'),
        ('lesson', '0013_auto_20160127_1321'),
    ]

    operations = [
        migrations.RenameModel('Questions', 'Question'),
        migrations.AddField(
            model_name='question',
            name='problem_solved',
            field=models.BooleanField(default=False),
        ),
    ]
