# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0003_auto_20150818_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroommenuitem',
            name='active',
            field=models.BooleanField(default=True, help_text='bestimmt, ob der Men\xfcpunkt im Kurzmen\xfc des Klassenzimmers\n            angezeigt werden soll.', verbose_name='aktiv'),
        ),
    ]
