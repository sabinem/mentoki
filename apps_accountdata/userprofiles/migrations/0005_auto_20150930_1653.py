# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0004_auto_20150930_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentorsprofile',
            name='display_nr',
            field=models.IntegerField(default=1, verbose_name='Anzeigereihenfolge'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mentorsprofile',
            name='text',
            field=models.TextField(verbose_name='ausf\xfchrliche Beschreibung', blank=True),
        ),
    ]
