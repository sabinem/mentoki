# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0010_auto_20150901_1604'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='announcement',
            name='archive',
        ),
        migrations.AddField(
            model_name='announcement',
            name='is_archived',
            field=models.BooleanField(default=False, help_text='Archivierte Ver\xf6ffentlichungen sind im Klassenzimmer nicht mehr zu sehen.\n        ', verbose_name='archivieren'),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='published',
            field=models.BooleanField(default=False, help_text='Beim Ver\xf6ffentlichen wird die Ank\xfcndigung an alle Kursteilnehmer\n        und Lehrer verschickt:\n        ', verbose_name='ver\xf6ffentlichen?'),
        ),
    ]
