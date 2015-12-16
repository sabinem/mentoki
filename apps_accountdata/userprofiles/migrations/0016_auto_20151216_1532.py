# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0015_mentorsprofile_is_ready'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentorsprofile',
            name='is_ready',
            field=models.BooleanField(default=False, verbose_name='fertig'),
        ),
    ]
