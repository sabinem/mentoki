# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_auto_20141212_2325'),
    ]

    operations = [
        migrations.RenameField(
            model_name='forum',
            old_name='description',
            new_name='text',
        ),
    ]
