# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_auto_20150419_1649'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='persondescription',
            new_name='qualification',
        ),
    ]
