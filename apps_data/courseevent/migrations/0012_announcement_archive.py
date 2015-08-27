# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0011_classroommenuitem_optional'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='archive',
            field=models.BooleanField(default=False, verbose_name='archivieren'),
        ),
    ]
