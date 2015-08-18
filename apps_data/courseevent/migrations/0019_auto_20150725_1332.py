# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0018_auto_20150725_1322'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentswork',
            old_name='user',
            new_name='workers',
        ),
    ]
