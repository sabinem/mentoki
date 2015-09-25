# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import fontawesome.fields


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='classlesson',
            name='icon',
            field=fontawesome.fields.IconField(max_length=60, blank=True),
        ),
        migrations.AddField(
            model_name='lesson',
            name='icon',
            field=fontawesome.fields.IconField(max_length=60, blank=True),
        ),
    ]
