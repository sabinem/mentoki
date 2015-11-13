# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0018_auto_20151113_1032'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseevent',
            name='autoslug',
            field=autoslug.fields.AutoSlugField(default='x', populate_from=('title', 'start_date'), editable=False),
            preserve_default=False,
        ),
    ]
