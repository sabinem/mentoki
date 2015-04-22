# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0026_auto_20150131_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursematerialunit',
            name='document_type',
            field=models.CharField(max_length=2, choices=[(b'g', b'PDF'), (b'1', b'normal'), (b't', b'Text')]),
            preserve_default=True,
        ),
    ]
