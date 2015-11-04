# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0008_auto_20151001_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentorsprofile',
            name='slug',
            field=models.SlugField(default='x'),
        ),
    ]
