# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='slug',
            field=autoslug.fields.AutoSlugField(populate_from='title', editable=False),
        ),
    ]
