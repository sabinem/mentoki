# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0002_auto_20150621_2213'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='announcement',
            options={'verbose_name': 'XAnnouncement'},
        ),
        migrations.AlterModelOptions(
            name='classrules',
            options={'verbose_name': 'Xclassrules'},
        ),
    ]
