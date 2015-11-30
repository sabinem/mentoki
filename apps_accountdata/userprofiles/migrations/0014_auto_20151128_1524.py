# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0013_auto_20151122_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentorsprofile',
            name='slug',
            field=autoslug.fields.AutoSlugField(populate_from='get_full_name', editable=False),
        ),
    ]
