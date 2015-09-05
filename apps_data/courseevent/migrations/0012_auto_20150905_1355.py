# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0011_auto_20150902_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroommenuitem',
            name='is_shortlink',
            field=models.BooleanField(default=False, help_text='die wichtigsten Links werden als Kurzlinks angezeigt.\n        Es sollte nicht mehr als 10 Kurzlinks geben', verbose_name='Kurzlink'),
        ),
    ]
