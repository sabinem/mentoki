# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0007_auto_20150427_0336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='courseevent',
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
