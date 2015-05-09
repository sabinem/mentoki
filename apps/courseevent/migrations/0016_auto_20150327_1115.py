# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0015_auto_20150219_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseevent',
            name='event_type',
            field=models.CharField(default=b'0', max_length=2, choices=[(b'0', b'Gruppenkurs'), (b'1', b'internes Diskussionsforum / ohne Termin / nicht gelistet '), (b'2', b'unbegleitetes Selbstlernen / ohne Termin'), (b'3', b'begleitetes Selbstlernen / ohne Termin')]),
            preserve_default=True,
        ),
    ]
