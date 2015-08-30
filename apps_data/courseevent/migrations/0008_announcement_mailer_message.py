# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailqueue', '0002_mailermessage_reply_to'),
        ('courseevent', '0007_auto_20150830_1248'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='mailer_message',
            field=models.ForeignKey(blank=True, to='mailqueue.MailerMessage', null=True),
        ),
    ]
