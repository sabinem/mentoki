# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import fontawesome.fields


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0002_auto_20150915_1208'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroommenuitem',
            name='icon',
            field=fontawesome.fields.IconField(max_length=60, blank=True),
        ),
    ]
