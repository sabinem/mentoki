# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0028_auto_20150207_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseunit',
            name='unit_type',
            field=models.CharField(default=b'l', max_length=2, choices=[(b'o', b'Organisation'), (b'l', b'Unterricht'), (b'', b'Normal'), (b'b', b'Bonusmaterial'), (b'c', b'Klassenliste'), (b'k', b'Kommunikation')]),
            preserve_default=True,
        ),
    ]
