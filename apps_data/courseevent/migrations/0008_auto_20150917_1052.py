# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0007_courseevent_email_greeting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseevent',
            name='email_greeting',
            field=models.CharField(help_text='Was soll im Betreff Feld stehen, wenn im Kurs\n        automatische Nachrichten f\xfcr diesen Kurs abgesetzt werden?', max_length=200, verbose_name='Email Betreff'),
        ),
        migrations.AlterField(
            model_name='courseevent',
            name='you_okay',
            field=models.BooleanField(default=True, help_text='Ist Duzen als Ansprache in Ordung in diesem Kurs?', verbose_name='Ansprache'),
        ),
    ]
