# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0003_classlesson_is_master'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classlesson',
            name='publish_status_changed',
        ),
        migrations.RemoveField(
            model_name='classlesson',
            name='published',
        ),
    ]
