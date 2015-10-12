# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_auto_20150605_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='title',
            field=models.CharField(help_text='Titel', max_length=100, verbose_name='Thema'),
        ),
    ]
