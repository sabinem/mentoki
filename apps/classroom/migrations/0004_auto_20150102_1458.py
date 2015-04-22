# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0003_auto_20141215_0542'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classrules',
            name='published_at_date',
        ),
        migrations.AlterField(
            model_name='classrules',
            name='status',
            field=models.CharField(default=b'0', max_length=2, choices=[(b'0', b'Entwurf'), (b'1', b'oeffentlich')]),
            preserve_default=True,
        ),
    ]
