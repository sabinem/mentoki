# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0008_courseevent_participant'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courseevent',
            old_name='participant',
            new_name='participants',
        ),
    ]
