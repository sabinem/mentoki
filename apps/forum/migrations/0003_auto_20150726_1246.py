# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20150621_2213'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='forum',
            options={'verbose_name': 'XForum'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'XPost'},
        ),
        migrations.AlterModelOptions(
            name='subforum',
            options={'verbose_name': 'XSubForum'},
        ),
        migrations.AlterModelOptions(
            name='thread',
            options={'verbose_name': 'XThread'},
        ),
    ]
