# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0024_auto_20150130_2233'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseunit',
            name='unit_type',
            field=models.CharField(default=b'', max_length=2, choices=[(b'o', b'Organisation'), (b'', b'Unterricht'), (b'b', b'Bonusmaterial'), (b'c', b'Klassenliste')]),
            preserve_default=True,
        ),
    ]
