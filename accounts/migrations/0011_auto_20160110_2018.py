# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20151216_1707'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='start_desk',
        ),
        migrations.AddField(
            model_name='user',
            name='notification_setting',
            field=models.IntegerField(default=3),
        ),
    ]
