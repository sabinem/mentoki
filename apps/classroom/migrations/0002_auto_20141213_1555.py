# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='announcement',
            name='publish_at_date',
        ),
        migrations.AddField(
            model_name='announcement',
            name='published',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='announcement',
            name='published_at_date',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='classrules',
            name='status',
            field=models.CharField(default=b'0', max_length=2, choices=[(b'0', b'Entwurf'), (b'1', b'veroeffentlicht'), (b'2', b'verfallen')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='classrules',
            name='publish_at_date',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
