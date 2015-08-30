# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0006_auto_20150830_0815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseevent',
            name='status_internal',
            field=models.CharField(default='0', max_length=2, verbose_name='interner Status', choices=[('0', 'nicht ver\xf6ffentlicht'), ('1', 'offen'), ('a', 'Vorschau')]),
        ),
    ]
