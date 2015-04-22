# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_auto_20150411_1310'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subforum',
            old_name='description',
            new_name='text',
        ),
    ]
