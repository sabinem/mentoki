# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mailqueue.models


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0009_auto_20150901_1538'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='announcement',
            name='send_to',
        ),
        migrations.AddField(
            model_name='announcement',
            name='mail_distributor',
            field=models.TextField(null=True, verbose_name=mailqueue.models.MailerMessage, blank=True),
        ),
    ]
