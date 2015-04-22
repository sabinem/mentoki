# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0002_auto_20141213_1555'),
    ]

    operations = [
        migrations.RenameField(
            model_name='classrules',
            old_name='publish_at_date',
            new_name='published_at_date',
        ),
    ]
