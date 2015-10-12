# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='generaltextchunks',
            name='text',
            field=froala_editor.fields.FroalaField(default='x'),
            preserve_default=False,
        ),
    ]
