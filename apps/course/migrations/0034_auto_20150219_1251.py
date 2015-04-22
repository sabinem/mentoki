# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0032_auto_20150219_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursematerialunit',
            name='document_type',
            field=models.CharField(default=b't', max_length=2, choices=[(b'g', b'PDF Viewer'), (b'1', b'PDF download und Text'), (b't', b'Text')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coursematerialunit',
            name='slug',
            field=models.SlugField(),
            preserve_default=True,
        ),
    ]
