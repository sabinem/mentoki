# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0008_announcement_mailer_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='announcement',
            name='mailer_message',
        ),
        migrations.AddField(
            model_name='announcement',
            name='send_to',
            field=models.TextField(blank=True),
        ),
    ]
