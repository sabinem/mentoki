# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0035_auto_20150811_2042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classroommenuitem',
            name='publish_status_changed',
        ),
        migrations.RemoveField(
            model_name='classroommenuitem',
            name='published',
        ),
    ]
