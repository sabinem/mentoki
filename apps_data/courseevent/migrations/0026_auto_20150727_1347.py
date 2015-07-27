# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0025_auto_20150727_1346'),
    ]

    operations = [
        migrations.RenameField(
            model_name='classroommenuitem',
            old_name='published_changed',
            new_name='publish_status_changed',
        ),
    ]
