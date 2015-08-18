# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0030_auto_20150805_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='description',
            field=models.CharField(help_text='Die Kurzbeschreibung erscheint auf der \xdcbersichtsseite der Foren.', max_length=200, verbose_name='Kurzbeschreibung', blank=True),
        ),
    ]
