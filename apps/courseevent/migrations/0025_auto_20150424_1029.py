# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0024_courseeventpubicinformation_excerpt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseevent',
            name='event_type',
            field=models.CharField(default='0', max_length=2, choices=[('0', 'gef\xfchrter Gruppenkurs'), ('1', 'internes Diskussionsforum / ohne Termin / nicht gelistet '), ('2', 'unbegleitetes Selbstlernen / ohne Termin'), ('3', 'begleitetes Selbstlernen / ohne Termin')]),
            preserve_default=True,
        ),
    ]
