# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0022_auto_20160107_2055'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['modified'], 'verbose_name': 'Post (Forum)', 'verbose_name_plural': 'Posts (Forum)'},
        ),
    ]
