# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0027_auto_20150206_2114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursematerialunit',
            name='document_is_rule',
        ),
        migrations.RemoveField(
            model_name='coursematerialunit',
            name='document_link',
        ),
        migrations.AlterField(
            model_name='coursematerialunit',
            name='document_type',
            field=models.CharField(max_length=2, choices=[(b'g', b'PDF Viewer'), (b'1', b'PDF download und Text'), (b't', b'Text')]),
            preserve_default=True,
        ),
    ]
